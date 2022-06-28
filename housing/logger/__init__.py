import logging
from datetime import datetime
import os

# Directory name to store all the log files
logdir = "housing_logs"

#Capturing the time when the pipeline will be triggered for naming the log files
current_time = f"{datetime.now().strftime('%d-%m-%Y_%H_%M_%S')}"

#Naming the log files
log_file_name = f"log_{current_time}.log"

#making the directory with the specified name
os.makedirs(logdir,exist_ok=True)

#complete path to the log file
log_file_path =os.path.join(logdir,log_file_name)

#setting up the logging configuration
logging.basicConfig(filename=log_file_path,
filemode="w",
format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
level=logging.INFO
)
