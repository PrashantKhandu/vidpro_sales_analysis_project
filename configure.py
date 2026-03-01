import os

current_path = os.getcwd()
os.makedirs(current_path + "/logs", exist_ok=True)
os.makedirs(current_path + "/logs/pandas_solutions", exist_ok=True)
os.makedirs(current_path + "/logs/sql_solutions", exist_ok=True)
os.makedirs(current_path + "/sample_data", exist_ok=True)
