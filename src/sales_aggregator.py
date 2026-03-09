import pandas as pd
import logging

def filter_april_sales(sales_df):

    valid_sales = []

    for _, row in sales_df.iterrows():

        try:
            date = pd.to_datetime(row["transaction_date"])

            if date.month != 4 or date.year != 2024:
                continue

            qty = row["quantity_sold"]

            if qty < 0:
                logging.warning("Negative quantity ignored")
                continue

            valid_sales.append(row)

        except Exception:
            logging.warning("Invalid transaction date ignored")

    return pd.DataFrame(valid_sales)


def aggregate_sales(sales_df):

    aggregated = (
        sales_df
        .groupby("product_id")["quantity_sold"]
        .sum()
        .reset_index()
    )

    aggregated.rename(
        columns={"quantity_sold": "total_sold_quantity"},
        inplace=True
    )

    return aggregated