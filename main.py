import pandas as pd
import pdfplumber
import re

class Product:
    def __init__(self, receipt_id, article_name, article_number, price_per_unit, quantity, unit, total_price):
        self.receipt_id = receipt_id
        self.article_name = article_name
        self.article_number = article_number
        self.price_per_unit = float(price_per_unit)
        self.quantity = float(quantity)
        self.unit = unit
        self.total_price = float(total_price)

def parse_receipt(receipt_path):
    try:
        with pdfplumber.open(receipt_path) as pdf:
            lines = []
            for i, page in enumerate(pdf.pages):

                text = page.extract_text()
                
                if i == 0:
                    store = re.search(r"ICA\s+\w+\s+\w+", text).group(0)
                    receipt_id = int(re.search(r"Kvitto nr\s+(\d+)", text).group(1))
                    date_str = re.search(r"Datum\s+(\d{4}-\d{2}-\d{2})", text).group(1)
                    time_str = re.search(r"Tid\s+(\d{2}:\d{2})", text).group(1)
                    datetime = pd.to_datetime(date_str + " " + time_str)

                lines.extend(text.split('\n'))

        for i, line in enumerate(lines):
                if "Beskrivning" in line:
                    header_index = i
                    break

        if header_index >= 0:
            end_index = len(lines)
            for i in range(header_index + 1, len(lines)):
                if "Betalat" in lines[i]:
                    end_index = i
                    break

        total_amount = float(lines[end_index].split()[-1].replace(",", "."))

        if header_index >= 0 and end_index > header_index:
            products = []
            for i in range(header_index + 1, end_index):
                line = lines[i].replace(",", ".").strip()
                parts = line.split()
                if "st" in parts or "kg" in parts and float(parts[-1]) > 0:
                    products.append(parts)

        parsed_products = []
        for product in products:
            name = " ".join(product[:-5])
            new_product = Product(receipt_id, name, product[-5], product[-4], product[-3], product[-2], product[-1])
            parsed_products.append(new_product)

        products_df = pd.DataFrame([product.__dict__ for product in parsed_products])
        receipts_df = pd.DataFrame({"receipt_id": [receipt_id], "store": [store], "datetime": [datetime], "total_amount": [total_amount]})
        return receipts_df, products_df
    except Exception as e:
        print(f"Error parsing receipt {receipt_path}: {e}")