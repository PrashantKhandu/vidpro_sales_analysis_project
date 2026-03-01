import datetime
import os

# project root folder
PROJECT_FOLDER_PATH = r"D:/Projects/vidpro_sales_analysis_project"

CONFIG_FOLDER = os.path.join(PROJECT_FOLDER_PATH, "custom_config")
LOG_FOLDER = os.path.join(PROJECT_FOLDER_PATH, "logs")
CONFIG_FILE = os.path.join(PROJECT_FOLDER_PATH, "custom_config", "config.ini")
OUTPUT_FOLDER = os.path.join(PROJECT_FOLDER_PATH, "sample_data")

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
