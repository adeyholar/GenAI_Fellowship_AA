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