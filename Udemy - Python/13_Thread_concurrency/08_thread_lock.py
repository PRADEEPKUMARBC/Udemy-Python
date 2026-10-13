import threading

counter = 0
lock = threading.Lock()

def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1