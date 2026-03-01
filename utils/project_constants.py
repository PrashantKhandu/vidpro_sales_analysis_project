import datetime
import os

current_path = os.getcwd()

# Required configuration files
CONFIG_FILE = os.path.join(current_path, "custom_config", "config.ini")
OUTPUT_FOLDER = os.path.join(current_path, "sample_data")

# File names
FILE_NAME = f"sales_analysis_data{str(datetime.datetime.now())[:-7].strip().replace(' ', '_')}"
#print(FILE_NAME)

# Log folder names
SQL_SOLUTIONS = "sql_solutions"
PANDAS_SOLUTIOINS = "pandas_solutions"

# Database & Table names
INTERVIEW = "interview"

CUSTOMERS = "customers"
SALES = "sales"
ITEMS = "items"
ORDERS = "orders"
