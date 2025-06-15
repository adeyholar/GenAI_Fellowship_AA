# Iterator example with network log lines
log_lines = ["2025-06-14 Router1 ERROR: Connection Lost",
             "2025-06-14 Switch1 OK: Stable",
             "2025-06-14 Router2 ERROR: Timeout"]

log_iterator = iter(log_lines)
print("Iterator next calls:")
print(next(log_iterator))  # First line
print(next(log_iterator))  # Second line
print(next(log_iterator))  # Third line
# print(next(log_iterator))  # Uncomment to see StopIteration

# Generator example for generating network log entries
def log_generator():
    yield "2025-06-14 Router1 ERROR: Connection Lost"
    yield "2025-06-14 Switch1 OK: Stable"
    yield "2025-06-14 Router2 ERROR: Timeout"

# Using the generator
log_gen = log_generator()
print("Generator next calls:")
print(next(log_gen))  # First entry
print(next(log_gen))  # Second entry
print(next(log_gen))  # Third entry
# print(next(log_gen))  # Uncomment to see StopIteration

# Practice exercise: Generator for network alert system
def network_alert_generator():
    alerts = [
        "ALERT: Router1 Down at 2025-06-14 09:00",
        "ALERT: Switch1 High Latency at 2025-06-14 09:05",
        "ALERT: Router2 Restored at 2025-06-14 09:10"
    ]
    for alert in alerts:
        yield alert
    while True:  # Infinite loop for continuous monitoring
        yield f"MONITORING: System check at {time.strftime('%Y-%m-%d %H:%M')}"

import time
# Using the generator with a limit
alert_gen = network_alert_generator()
print("Network alerts:")
for _ in range(5):  # Limit to 5 alerts to avoid infinite loop
    print(next(alert_gen))