import unittest
import pandas as pd
from src.inventory_engine import stock_status

class TestInventoryEngine(unittest.TestCase):

    def test_available_status(self):

        self.assertEqual(stock_status(20),"AVAILABLE")

    def test_low_stock_status(self):

        self.assertEqual(stock_status(5),"LOW_STOCK")

    def test_out_of_stock_status(self):

        self.assertEqual(stock_status(0),"OUT_OF_STOCK")

if __name__ == "__main__":
    unittest.main()