# Basic exception handling for file reading
try:
    with open("network_log.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: network_log.txt not found. Creating a sample file.")
    with open("network_log.txt", "w") as file:
        file.write("2025-06-14 Router1 ERROR: Connection Lost")
    print("Sample file created. Please run again.")