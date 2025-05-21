# Grocery Spend EDA

Exploratory Data Analysis of my personal grocery spend data for the past ~3 years.

## Process

Every purchase I make at an ICA store sends the receipt to the Kivra app, where you can download each individual receipt as a pdf. I downloaded all of my receipts and made a parser that creates two dataframes, one for each receipt itself, and one for all of the purchased items in the receipts.

#### receipts_df:

| receipt_id | store | datetime | total_amount |
| ---------- | ----- | -------- | ------------ |

#### products_df:

| receipt_id | article_name | article_number | price_per_unit | quantity | unit | total_price |
| ---------- | ------------ | -------------- | -------------- | -------- | ---- | ----------- |

## Findings

Over the last two years my monthly average spending has increased by over 1000 SEK (33%). Looking at the quantity during this time suggests that I am simply buying more, as it also increased in a similar fashion and the weighted average price has remained fairly constant.

## Graphs

![Day Percentages](data/output/day_percentages.png)

![Time of Day Percentages](data/output/time_of_day_percentages.png)

![Day and Time Heatmap](data/output/day_time_heatmap.png)

![Weekly Spend](data/output/weekly_spend.png)

![Monthly Spend](data/output/monthly_spend.png)

![Monthly Quantity](data/output/monthly_quantity.png)

![Monthly Weighted Average Price](data/output/monthly_weighted_average_price.png)

![Distribution of Days Between Store Visits](data/output/visit_gap_distribution.png)

![Distribution of Total Amounts](data/output/amount_bracket_distribution.png)

![Total Amount Days Between Heatmap](data/output/amount_days_between_heatmap.png)
