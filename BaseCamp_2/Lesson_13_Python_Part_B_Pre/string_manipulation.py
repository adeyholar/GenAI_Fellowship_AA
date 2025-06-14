# Basic string operations with network log example
log_entry = "2025-06-14 Router1 ERROR: Connection Lost"
print("Original log:", log_entry)

# Split into components
parts = log_entry.split()
print("Split parts:", parts)

# Join with a different delimiter
new_log = ":".join(parts)
print("Joined with colon:", new_log)

# Uppercase for consistency
upper_log = log_entry.upper()
print("Uppercase log:", upper_log)

# String formatting for network status
device = "Router1"
status = "Up"
formatted_status = f"Device {device} is {status} at {log_entry[:10]}"
print("Formatted status:", formatted_status)

# Using .format()
formatted_alt = "Device {} is {} at {}".format(device, status, log_entry[:10])
print("Formatted alternative:", formatted_alt)

# String methods for cleaning
dirty_log = "  2025-06-14  Router1  ERROR:  Connection  Lost  "
cleaned_log = dirty_log.strip()  # Remove leading/trailing spaces
print("Cleaned log:", cleaned_log)

# Replace unwanted text
sanitized_log = cleaned_log.replace("ERROR:", "ISSUE:")
print("Sanitized log:", sanitized_log)

# Check substring
has_error = "ERROR" in cleaned_log
print("Contains ERROR:", has_error)