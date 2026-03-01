from pandas import DataFrame
import pandas as pd
import traceback
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from custom_library.init_logger import get_logger
from custom_library.init_postgres_connection import get_new_postgreSQL_connection
from project_constants import *

def process_sales_data(customers:DataFrame, orders:DataFrame, items:DataFrame, sales:DataFrame):
    """Processing the data with validating, grouping, and filtering"""
    # Merging all tables
    df = sales.merge(orders, on="order_id").merge(customers, on="customer_id").merge(items, on="item_id")

    # Grouping and aggregating
    result = df.groupby(["customer_name", "age", "item_name"], as_index=False)["quantity"].sum()

    # Remove rows where: sum is 0/NaN
    result = result[(result["quantity"].notna()) & (result["quantity"] > 0)]

    # Rename columns to match required CSV header
    result = result.rename(columns={
        "customer_name": "Customer",
        "age": "Age",
        "item_name": "Item",
        "quantity": "Quantity"
    })

    # No decimals check
    result["Quantity"] = result["Quantity"].astype(int)
    return result

def load_data():
    """This func loads the data from given tables(We can filter the data based on requirements)"""
    logger = get_logger()
    try:
        logger.info("Connecting to interview database...")
        connection = get_new_postgreSQL_connection()

        customer_query = "SELECT * FROM customer;"
        orders_query = "SELECT * FROM orders;"
        items_query = "SELECT * FROM items;"
        sales_query = "SELECT * FROM sales;"

        customer = pd.read_sql(customer_query, connection)
        orders = pd.read_sql(orders_query, connection)
        items = pd.read_sql(items_query, connection)
        sales = pd.read_sql(sales_query, connection)

        logger.info("Data successfully loaded from database.")
        return customer, orders, items, sales
    except Exception as e:
        logger.error(f"Error loading data from database: {e}")
        logger.error(traceback.format_exc())
        raise
    finally:
        if connection:
            connection.close()
            logger.info("Database connection closed.")

def write_csv(df:DataFrame):
    """This function writes the data into CSV fiile"""
    logger = get_logger()
    try:
        write_file_name = f"{OUTPUT_FOLDER}/{FILE_NAME}.csv"
        df.to_csv(write_file_name, sep=";", index=False)
    except Exception as e:
        logger.error(f"CSV writing error: {e}")
        logger.error(traceback.format_exc())

def main():
    """
    This is a main function
    Description:
        - Loading data from database
        - Processing the data
        - Final data writing into csv file
    """
    logger = get_logger()
    try:
        logger.info("Data loading started from Postgres to DF")
        customer, orders, items, sales = load_data()
        logger.info("Data processing started")
        result = process_sales_data(customer, orders, items, sales)
        write_csv(result)
        logger.info("Pandas solution executed successfully.")
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    logger = get_logger(PANDAS_SOLUTIOINS)
    try:
        main()
    except Exception as e:
        logger.error(f"Program execution failed due to {e}")
        logger.error(traceback.format_exc())
