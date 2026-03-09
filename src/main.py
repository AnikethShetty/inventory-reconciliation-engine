from loader import load_inventory, load_sales
from sales_aggregator import filter_april_sales, aggregate_sales
from inventory_engine import reconcile_inventory
from reporter import export_inventory_csv, export_summary_json

def main():

    inventory = load_inventory("../data/inventory.csv")
    sales = load_sales("../data/sales_transactions.csv")

    filtered_sales = filter_april_sales(sales)

    aggregated_sales = aggregate_sales(filtered_sales)

    final_inventory = reconcile_inventory(inventory, aggregated_sales)

    export_inventory_csv(final_inventory)

    export_summary_json(
        final_inventory,
        len(filtered_sales)
    )

    print("Inventory reconciliation completed.")

if __name__ == "__main__":
    main()