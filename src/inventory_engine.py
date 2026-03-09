import logging

def reconcile_inventory(inventory_df, sales_df):

    merged = inventory_df.merge(
        sales_df,
        on="product_id",
        how="left"
    )

    merged["total_sold_quantity"] = merged["total_sold_quantity"].fillna(0)

    merged["final_stock"] = (
        merged["current_stock"] - merged["total_sold_quantity"]
    )

    merged.loc[merged["final_stock"] < 0, "final_stock"] = 0

    merged["stock_status"] = merged["final_stock"].apply(stock_status)

    merged["total_sales_value"] = (
        merged["total_sold_quantity"] * merged["unit_price"]
    )

    return merged


def stock_status(stock):

    if stock == 0:
        return "OUT_OF_STOCK"

    elif 1 <= stock <= 10:
        return "LOW_STOCK"

    else:
        return "AVAILABLE"