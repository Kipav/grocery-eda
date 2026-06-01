# Grocery Spend EDA

Exploratory Data Analysis of my personal grocery spending over the past three years.

## Overview

This project analyzes all my grocery purchases from ICA stores using receipt data collected via the Kivra app. It includes data extraction, preprocessing, exploratory analysis in Python, and interactive dashboards created in Power BI.

## Data Collection

Every purchase I make at an ICA store sends a receipt to the Kivra app. These receipts are downloadable as PDFs. I built a custom parser to extract data from these receipts into two structured DataFrames:

#### receipts_df:

| receipt_number | datetime |
| -------------- | -------- |

#### products_df:

| receipt_number | item_name | item_id | unit_price | quantity | unit | pre_discount_sum |
| -------------- | --------- | ------- | ---------- | -------- | ---- | ---------------- |

## Process

1. Data Extraction: Receipt PDFs were parsed into structured tabular data.

2. Initial EDA: Conducted in Python using pandas, matplotlib, and seaborn.

3. Modeling & Dashboards: Data was normalized and imported into Power BI for further analysis and dashboard creation.

## Key Findings

- Monthly Spend Increase: Over the last two years, my average monthly spend increased by more than 1000 SEK (approx. 33%).
- Quantity vs. Price: The increased spend is mostly due to buying more items. The weighted average price has remained relatively stable.

## Power BI Dashboards

### Visits

![Visits](data/graphs/powerbi_1.png)

### Spending

![Spending](data/graphs/powerbi_2.png)

### Quantity

![Quantity](data/graphs/powerbi_3.png)

## Python Graphs

![Day Percentages](data/graphs/day_percentages.png)

![Time of Day Percentages](data/graphs/time_of_day_percentages.png)

![Day and Time Heatmap](data/graphs/day_time_heatmap.png)

![Weekly Spend](data/graphs/weekly_spend.png)

![Monthly Spend](data/graphs/monthly_spend.png)

![Monthly Quantity](data/graphs/monthly_quantity.png)

![Monthly Weighted Average Price](data/graphs/monthly_weighted_average_price.png)

![Distribution of Days Between Store Visits](data/graphs/visit_gap_distribution.png)

![Distribution of Total Amounts](data/graphs/amount_bracket_distribution.png)

![Total Amount Days Between Heatmap](data/graphs/amount_days_between_heatmap.png)