import traceback
import csv
import sys
import os

sys.path.append(os.getcwd())

from ..custom_library.init_postgres_connection import get_new_postgreSQL_connection
from ..custom_library.init_logger import get_logger
from ..utils.project_constants import *

logger = None
connection = None

def fetch_data():
    logger = get_logger()
    query = """
        SELECT 
            c.customer_name,
            c.age,
            i.item_name,
            SUM(s.quantity) AS quantity
        FROM sales s
        JOIN orders o
            ON s.order_id = o.order_id
        JOIN customer c 
            ON o.customer_id = c.customer_id
        JOIN items i 
            ON s.item_id = i.item_id
        GROUP BY c.customer_name, c.age, i.item_name
        HAVING SUM(s.quantity) IS NOT NULL AND SUM(s.quantity) > 0
        ORDER BY c.customer_name, i.item_name;
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            headers = [desc[0].capitalize() for desc in cursor.description]
            return headers, rows
    except Exception as e:
        logger.error("Query execution error:", e)
        logger.error("Traceback: ", traceback.format_exc())
        sys.exit(1)

def write_csv(headers, rows):
    logger = get_logger()
    try:
        write_file_path = f"{OUTPUT_FOLDER}/{FILE_NAME}.csv"
        with open(write_file_path, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(headers)
            for row in rows:
                writer.writerow([
                    row[0],
                    row[1],
                    row[2],
                    int(row[3])
                ])
    except Exception as e:
        logger.error("CSV writing error:", e)
        logger.error(traceback.format_exc())
        sys.exit(1)

def main():
    logger = get_logger()
    global connection
    try:
        logger.info(f"Data fetching starting...")
        headers, rows = fetch_data(connection)
        logger.info(f"Data fetching completed")
        logger.info(f"Got {len(rows)} rows")
        logger.info(f"Data writing starting...")
        write_csv(headers, rows)
        logger.info("Data write into csv file completed")
    except Exception as e:
        logger.critical(e)
        logger.error(traceback.format_exc())


if __name__ == "__main__":
    logger = get_logger(SQL_SOLUTIONS)
    connection = get_new_postgreSQL_connection(dbname=INTERVIEW)
    try:
        logger.info("Program execution started")
        main()
        logger.info("Program exection completed successfully")
    except Exception as e:
        logger.error(f"Program execution failed due to {e}")
        logger.error(traceback.format_exc())
    finally:
        connection.close()
