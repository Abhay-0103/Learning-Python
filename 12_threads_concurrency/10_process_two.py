from multiprocessing import Process
import time

def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10**7):
        total += i
    print("DONE BIDU KYA BOTHE")

if __name__ == "__main__":
    start = time.time()

    processes = [Process(target=cpu_heavy) for _ in range(2)]

    # Start all processes
    for p in processes:
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print(f"Time Taken: {time.time() - start:.2f} seconds")