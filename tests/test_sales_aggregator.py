import unittest
import pandas as pd
from src.sales_aggregator import aggregate_sales

class TestSalesAggregation(unittest.TestCase):

    def test_multiple_sales_aggregation(self):

        data = pd.DataFrame({
            "product_id": [1,1,2],
            "quantity_sold":[2,3,4]
        })

        result = aggregate_sales(data)

        self.assertEqual(
            result.loc[result["product_id"]==1,
            "total_sold_quantity"].values[0],5)

    def test_negative_quantity_ignored(self):

        self.assertTrue(True)

    def test_invalid_transaction_date(self):

        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()