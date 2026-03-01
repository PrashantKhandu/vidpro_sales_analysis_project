import configparser
import sys, os

sys.path.append(os.getcwd())
from init_logger import get_logger
from ..project_constants import CONFIG_FILE

def get_configuration(*args:str):
    logger = get_logger()
    if not os.path.exists(CONFIG_FILE):
        logger.critical(f"config.ini file doesn't exist in {CONFIG_FILE}")
        exit()

    args = [arg.upper() for arg in args]
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    config_map = {
        "P_USERNAME":config.get("POSTGRESQL", "username"),
        "P_HOST":config.get("POSTGRESQL", "host"),
        "P_PORT":config.get("POSTGRESQL", "port"),
        "P_PASSWORD":config.get("POSTGRESQL", "password"),
    }
    return tuple(config_map[arg] for arg in args if arg in config_map)

if __name__ == "__main__":
    print("This is configuration file.")
