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

# Handling multiple exceptions
try:
    with open("network_log.txt", "r") as file:
        content = file.read()
        number = int(content.split()[0])  # Try to convert first word to int
except FileNotFoundError:
    print("Error: network_log.txt not found. Creating a sample file.")
    with open("network_log.txt", "w") as file:
        file.write("2025-06-14 Router1 ERROR: Connection Lost")
    print("Sample file created. Please run again.")
except ValueError:
    print("Error: Invalid data format in network_log.txt. Please check the content.")
except Exception as e:
    print(f"Unexpected error: {e}")

# Practice exercise: Network log parser with exception handling
def parse_network_log(log_file):
    try:
        with open(log_file, "r") as file:
            logs = file.readlines()
            for log in logs:
                parts = log.strip().split()
                if len(parts) < 2:
                    raise ValueError("Invalid log format: too few fields")
                timestamp, device = parts[0], parts[1]
                status = " ".join(parts[2:]) if len(parts) > 2 else "Unknown"
                print(f"Parsed: {timestamp} - {device} - {status}")
    except FileNotFoundError:
        print(f"Error: {log_file} not found. Please create the file.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Test with an existing file and a modified one
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "network_log.txt")
parse_network_log(log_file)

# Simulate a bad log by modifying network_log.txt (e.g., add a line with "2025-06-14")
with open(log_file, "a") as file:
    file.write("\n2025-06-14")  # Invalid format
parse_network_log(log_file)