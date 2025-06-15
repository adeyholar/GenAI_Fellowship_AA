# Basic exception handling for file reading
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "network_log.txt")

try:
    with open(log_file, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: network_log.txt not found. Creating a sample file.")
    with open(log_file, "w") as file:
        file.write("2025-06-14 Router1 ERROR: Connection Lost")
    print("Sample file created. Please run again.")