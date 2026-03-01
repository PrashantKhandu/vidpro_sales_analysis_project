from psycopg2 import errors
import psycopg2
import sys
import os

sys.path.append(os.getcwd())
from get_configurations import *

def get_new_postgreSQL_connection(dbname: str):
    """
    Description : Configurations for creating connection to postgre-sql
            This function returns connection and cursor of postgre sql database for passed dbname only
    Mandatory : Finally must close the cursor and connection respectively
    """
    logger = get_logger()
    hostname, port, username, password = get_configuration("P_HOST", "P_PORT", "P_USERNAME", "P_PASSWORD")
    try:
        connection = psycopg2.connect(dbname=dbname, user=username, password=password, host=hostname, port=int(port))
        logger.debug("Postgre-SQL is Active")
        logger.info("New Postgre-SQL connection connected to {}".format(hostname))
        logger.info("New connection created to Postgre-SQL Database.")
        return connection
    except Exception as e:
        logger.critical("PostgreSQL is Inactive or Failed. Exiting")
        exit()

if __name__ == "__main__":
    print("This is various DB connections file.")
