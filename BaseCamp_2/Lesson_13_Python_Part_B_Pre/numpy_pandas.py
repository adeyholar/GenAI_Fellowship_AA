import numpy as np

# Network latency data in milliseconds
latency_data = [10, 15, 20, 25, 30]
latency_array = np.array(latency_data)
print("Latency array:", latency_array)

# Basic operations
mean_latency = np.mean(latency_array)
max_latency = np.max(latency_array)
print("Mean latency:", mean_latency)
print("Max latency:", max_latency)

import pandas as pd

# Network device data as a DataFrame
data = {
    "Device": ["Router1", "Switch1", "Router2"],
    "Status": ["Up", "Down", "Up"],
    "Latency": [10, 15, 20]
}
df = pd.DataFrame(data)
print("Network DataFrame:")
print(df)

# Basic operations
average_latency = df["Latency"].mean()
up_devices = df[df["Status"] == "Up"]
print("\nAverage latency:", average_latency)
print("Devices that are Up:")
print(up_devices)

# Practice exercise: Network performance analysis
# Sample data with more devices and metrics
data = {
    "Device": ["Router1", "Switch1", "Router2", "Switch2"],
    "Status": ["Up", "Down", "Up", "Up"],
    "Latency": [10, 15, 20, 25],
    "PacketLoss": [0.1, 0.5, 0.2, 0.0]
}
df = pd.DataFrame(data)

# Convert Latency and PacketLoss to NumPy arrays for analysis
latency_array = df["Latency"].to_numpy()
packet_loss_array = df["PacketLoss"].to_numpy()

# Calculate statistics
mean_latency = np.mean(latency_array)
max_packet_loss = np.max(packet_loss_array)
healthy_devices = df[(df["Status"] == "Up") & (df["PacketLoss"] < 0.3)]

print("\nNetwork Performance Analysis:")
print("DataFrame:")
print(df)
print(f"\nMean Latency: {mean_latency} ms")
print(f"Max Packet Loss: {max_packet_loss}%")
print("Healthy Devices (Up and <0.3% Packet Loss):")
print(healthy_devices)