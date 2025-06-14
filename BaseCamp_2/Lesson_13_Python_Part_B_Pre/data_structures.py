# Dictionary of device statuses
device_status = {"Router1": "Up", "Switch1": "Down", "Router2": "Up"}
print("Device statuses:", device_status)

# Update a status
device_status["Switch1"] = "Up"
print("After update:", device_status)

# Access a value
print("Router1 status:", device_status["Router1"])