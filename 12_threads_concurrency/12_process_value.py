from multiprocessing import Process, Queue, Value

def increment(counter):
    for _ in range(100_000):
        with counter.get_lock():
            counter.value += 1



if __name__ == "__main__":
    counter = Value('i', 0)
    Processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in Processes]
    [p.join() for p in Processes]

    print("Final counter.value: ", counter.value)