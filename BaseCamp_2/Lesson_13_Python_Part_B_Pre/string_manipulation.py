# Basic string operations
log_entry = "2025-06-14 Router1 ERROR: Connection Lost"
print("Original log:", log_entry)
parts = log_entry.split()
print("Split parts:", parts)
new_log = ":".join(parts)
print("Joined with colon:", new_log)
upper_log = log_entry.upper()
print("Uppercase log:", upper_log)

# String formatting
device = "Router1"
status = "Up"
formatted_status = f"Device {device} is {status} at {log_entry[:10]}"
print("Formatted status:", formatted_status)
formatted_alt = "Device {} is {} at {}".format(device, status, log_entry[:10])
print("Formatted alternative:", formatted_alt)

# String methods
dirty_log = "  2025-06-14  Router1  ERROR:  Connection  Lost  "
cleaned_log = dirty_log.strip()
print("Cleaned log:", cleaned_log)
sanitized_log = cleaned_log.replace("ERROR:", "ISSUE:")
print("Sanitized log:", sanitized_log)
has_error = "ERROR" in cleaned_log
print("Contains ERROR:", has_error)

# Practice exercise
def process_logs(log_list):
    cleaned_logs = [log.strip().replace("ERROR:", "ISSUE:").upper() for log in log_list]
    return cleaned_logs

logs = [
    "  2025-06-14 Router1 ERROR: Connection Lost  ",
    "2025-06-14 Switch1 OK: Stable",
    "  2025-06-14 Router2 ERROR: Timeout  "
]
processed = process_logs(logs)
print("Processed logs:", processed)