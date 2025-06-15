import threading
import time
import multiprocessing

def ping_device(device):
    print(f"Starting ping for {device} at {time.strftime('%H:%M:%S')}")
    time.sleep(2)
    print(f"Finished ping for {device} at {time.strftime('%H:%M:%S')}")

devices = ["Router1", "Switch1", "Router2"]
threads = []
for device in devices:
    t = threading.Thread(target=ping_device, args=(device,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All pings completed.")

def process_data(device):
    print(f"Processing data for {device} at {time.strftime('%H:%M:%S')}")
    time.sleep(2)
    result = sum(range(1000000))
    print(f"Completed processing for {device} at {time.strftime('%H:%M:%S')} with result: {result}")

if __name__ == "__main__":
    devices = ["Router1", "Switch1", "Router2"]
    processes = []
    for device in devices:
        p = multiprocessing.Process(target=process_data, args=(device,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed.")