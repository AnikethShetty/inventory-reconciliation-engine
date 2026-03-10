import unittest
import pandas as pd
from src.inventory_engine import reconcile_inventory, stock_status


class TestInventoryEngine(unittest.TestCase):

    # ----------------------------------------
    # INVENTORY CALCULATION TESTS
    # ----------------------------------------

    # TEST CASE 4: Inventory Reduction
    def test_inventory_reduction(self):

        inventory = pd.DataFrame({
            "product_id": [1],
            "product_name": ["Product A"],
            "current_stock": [20],
            "unit_price": [10],
            "category": ["Electronics"]
        })

        sales = pd.DataFrame({
            "product_id": [1],
            "total_sold_quantity": [5]
        })

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result.loc[0, "final_stock"], 15)


    # TEST CASE 5: Inventory Not Negative
    def test_inventory_not_negative(self):

        inventory = pd.DataFrame({
            "product_id": [1],
            "product_name": ["Product A"],
            "current_stock": [5],
            "unit_price": [10],
            "category": ["Electronics"]
        })

        sales = pd.DataFrame({
            "product_id": [1],
            "total_sold_quantity": [10]
        })

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result.loc[0, "final_stock"], 0)


    # TEST CASE 6: Zero Stock Status
    def test_zero_stock_status(self):

        self.assertEqual(stock_status(0), "OUT_OF_STOCK")


    # ----------------------------------------
    # STOCK STATUS TESTS
    # ----------------------------------------

    # TEST CASE 7: Available Status
    def test_available_status(self):

        self.assertEqual(stock_status(20), "AVAILABLE")


    # TEST CASE 8: Low Stock Status
    def test_low_stock_status(self):

        self.assertEqual(stock_status(5), "LOW_STOCK")


    # TEST CASE 9: Out of Stock Status
    def test_out_of_stock_status(self):

        self.assertEqual(stock_status(0), "OUT_OF_STOCK")


if __name__ == "__main__":
    unittest.main()