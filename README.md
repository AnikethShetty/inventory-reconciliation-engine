# Inventory Reconciliation & Sales Analysis Engine

## Project Overview
This project implements an **Inventory Reconciliation and Sales Analysis Engine** developed in Python.

The system processes product inventory and sales transaction data to reconcile stock levels, detect stock issues, and generate sales reports.

The application follows modular design principles and includes logging, error handling, and unit testing.


## Business Problem

An e-commerce company maintains product inventory and daily sales transactions.  
Manual reconciliation of stock levels is time-consuming and error-prone.

This system automates:

• Sales transaction validation  
• Sales aggregation  
• Inventory reconciliation  
• Stock status identification  
• Sales reporting


## Key Features

### 1. Data Processing
- Reads inventory and sales data from CSV files
- Processes only **April 2024 transactions**

### 2. Sales Aggregation
- Aggregates total sales per product
- Detects invalid transactions

### 3. Inventory Reconciliation
Final stock is calculated as:

final_stock = current_stock - total_quantity_sold

### 4. Stock Status Detection

| Final Stock | Status |
|-------------|--------|
| 0 | OUT_OF_STOCK |
| 1 – 10 | LOW_STOCK |
| > 10 | AVAILABLE |

### 5. Report Generation
The system generates:

**1. inventory_reconciliation.csv**

Columns:
- product_id
- product_name
- category
- current_stock
- total_sold_quantity
- final_stock
- stock_status
- total_sales_value

**2. sales_summary.json**

Metrics:
- total_products
- total_transactions_processed
- total_sales_value
- low_stock_products
- out_of_stock_products


## Project Structure

inventory_project
│
├── data
│   ├── inventory.csv
│   ├── sales_transactions.csv
│
├── src
│   ├── loader.py
│   ├── sales_aggregator.py
│   ├── inventory_engine.py
│   ├── reporter.py
│   └── main.py
│
├── tests
│   ├── test_sales_aggregator.py
│   ├── test_inventory_engine.py
│
├── logs
│   └── inventory.log
│
├── inventory_reconciliation.csv
├── sales_summary.json
└── README.md


## Technologies Used

- Python
- Pandas
- JSON
- CSV Processing
- Logging
- Unit Testing (unittest)


## Business Rules Implemented

### Sales Filtering
- Only transactions from **April 2024** are processed
- Invalid transaction dates are ignored and logged
- Negative quantities are ignored

### Sales Validation
- Transactions with unknown product IDs are logged

### Inventory Reconciliation
- Inventory updated after aggregating sales
- Negative stock values prevented

### Error Handling
The system handles:
- Invalid dates
- Missing product IDs
- Negative sales quantities
- Corrupt data

The application continues running without crashing.


## Installation

### Step 1 — Install Python

Download Python from:
https://www.python.org

### Step 2 — Install Dependencies

Run:

pip install pandas


## How to Run the Application

Open terminal in the project folder.

Run:

cd src
python main.py

Output files will be generated:

inventory_reconciliation.csv
sales_summary.json


## Running Unit Tests

Run the following command:

python -m unittest discover tests


## Edge Cases Handled

The system safely handles:

- Invalid transaction dates
- Unknown product IDs
- Negative sales quantities
- Missing sales data
- Stock values going below zero


## Author

Aniketh S. Shetty  
B.Tech Computer Science & Engineering  
Srinivas University Institute of Engineering and Technology


## License

This project is developed for internship and academic purposes.