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

![Spending by Category](data/graphs/spending_by_category.png)
