import json

def export_inventory_csv(df):

    output = df[
        [
            "product_id",
            "product_name",
            "category",
            "current_stock",
            "total_sold_quantity",
            "final_stock",
            "stock_status",
            "total_sales_value",
        ]
    ]

    output.to_csv(
        "../inventory_reconciliation.csv",
        index=False
    )


def export_summary_json(df, total_transactions):

    summary = {
        "total_products": len(df),
        "total_transactions_processed": total_transactions,
        "total_sales_value": float(df["total_sales_value"].sum()),
        "low_stock_products": int((df["stock_status"] == "LOW_STOCK").sum()),
        "out_of_stock_products": int((df["stock_status"] == "OUT_OF_STOCK").sum())
    }

    with open("../sales_summary.json", "w") as f:
        json.dump(summary, f, indent=4)