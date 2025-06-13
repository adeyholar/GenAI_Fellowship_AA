import multiprocessing
import time

def compute_heavy_task(n):
    result = 0
    for i in range(n):
        result += i ** 2  # Simulate CPU-intensive calculation
    return result

if __name__ == '__main__':
    # Number of tasks and size
    num_tasks = 4
    task_size = 10_000_000

    # Sequential execution
    start_time = time.time()
    results = [compute_heavy_task(task_size) for _ in range(num_tasks)]
    sequential_time = time.time() - start_time
    print(f"Sequential execution time: {sequential_time:.2f} seconds")

    # Multiprocessing execution
    start_time = time.time()
    processes = []
    for _ in range(num_tasks):
        p = multiprocessing.Process(target=compute_heavy_task, args=(task_size,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing execution time: {multiprocessing_time:.2f} seconds")
    print(f"Speedup factor: {sequential_time / multiprocessing_time:.2f}x")