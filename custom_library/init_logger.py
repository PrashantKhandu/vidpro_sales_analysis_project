# This configuration for logging
import traceback
import logging
import logging.config
import sys
import os

sys.path.append(os.getcwd())
from get_configurations import *

g_logger = None
g_logger_name = None

def get_logger(logger_name=None):
    if logger_name:
        os.makedirs(os.path.join("logs", logger_name), exist_ok=True)
    global g_logger, g_logger_name
    if g_logger == None:
        # this means get_logger is inovked for the first time
        if logger_name != None:
            g_logger_name = logger_name
        else:
            # when invoked for the first time, get_logger must be supplied with the logger name
            logging.config.fileConfig(os.path.join("logger_config.conf"), {"filename": os.path.join("logs", "default", "default" + ".log").replace("\\", "/")})
            logger = logging.getLogger("default")
            logger.warning("Logger name must be provided when logger is initialized for first time. Using the default",)
            stack = traceback.format_stack()
            stack = "Invoked by: ".join(stack)
            logger.warning(stack)
            return logger

        logging.config.fileConfig(
            os.path.join("logger_config.conf"), {"filename": os.path.join("osint", "logs", g_logger_name, g_logger_name + ".log").replace("\\", "/")})
        g_logger = logging.getLogger(g_logger_name)
    elif logger_name != None:
        # when invoked second time or later, log a warning message if logger name is supplied again.
        g_logger.warning("Logger initialization invoked multiple times, ignoring...")
        stack = traceback.format_stack()
        stack = "Invoked by: ".join(stack)
        g_logger.debug(stack)
    return g_logger

def get_logger_name():
    global g_logger_name
    return g_logger_name
