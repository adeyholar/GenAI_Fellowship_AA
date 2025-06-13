from network_utils import parse_network_log, check_device_status, count_log_issues

# Test log parsing
log_entry = "2025-06-13 Router1 WARNING: High Latency"
print(parse_network_log(log_entry))

# Test device status
print(check_device_status())

# Test counting issues
logs = [
    "2025-06-13 Router1 ERROR: Connection Lost",
    "2025-06-13 Router2 OK: Stable",
    "2025-06-13 Switch1 CRITICAL: Overload"
]
issue_count = count_log_issues(logs)
print(f"Total issues: {issue_count}")  # Expected: Total issues: 2