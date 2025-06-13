import threading
import time
import os

def read_file(file_name, delay):
    time.sleep(delay)  # Simulate I/O delay
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name), 'w') as f:
        f.write(f"Data from {file_name} at {time.ctime()}")
    print(f"Finished reading {file_name}")

# List of files to simulate I/O
files = ['file1.txt', 'file2.txt', 'file3.txt']
delays = [2, 1, 3]  # Simulated delays in seconds

# Sequential execution
start_time = time.time()
for file, delay in zip(files, delays):
    read_file(file, delay)
sequential_time = time.time() - start_time
print(f"Sequential execution time: {sequential_time:.2f} seconds")

# Threaded execution
start_time = time.time()
threads = []
for file, delay in zip(files, delays):
    t = threading.Thread(target=read_file, args=(file, delay))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
threaded_time = time.time() - start_time
print(f"Threaded execution time: {threaded_time:.2f} seconds")
print(f"Speedup factor: {sequential_time / threaded_time:.2f}x")