import unittest
import pandas as pd
from src.sales_aggregator import aggregate_sales, filter_april_sales


class TestSalesAggregator(unittest.TestCase):

    # ----------------------------------------
    # TEST CASE 1: Multiple Sales Aggregation
    # ----------------------------------------
    def test_multiple_sales_aggregation(self):

        data = pd.DataFrame({
            "product_id": [1, 1, 2],
            "quantity_sold": [2, 3, 4]
        })

        result = aggregate_sales(data)

        self.assertEqual(
            result.loc[result["product_id"] == 1, "total_sold_quantity"].values[0],
            5
        )

    # ----------------------------------------
    # TEST CASE 2: Invalid Transaction Date
    # ----------------------------------------
    def test_invalid_transaction_date(self):

        data = pd.DataFrame({
            "product_id": [1],
            "transaction_date": ["invalid-date"],
            "quantity_sold": [5]
        })

        result = filter_april_sales(data)

        self.assertEqual(len(result), 0)

    # ----------------------------------------
    # TEST CASE 3: Negative Quantity Ignored
    # ----------------------------------------
    def test_negative_quantity_ignored(self):

        data = pd.DataFrame({
            "product_id": [1],
            "transaction_date": ["2024-04-10"],
            "quantity_sold": [-5]
        })

        result = filter_april_sales(data)

        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()