import threading
import time

def prepare_chai(type, wait_time):
    print(f"{threading.current_thread().name} started preparing {type} chai ....")
    time.sleep(wait_time)
    print(f"{threading.current_thread().name} finished preparing {type} chai ....")


t1 = threading.Thread(target=prepare_chai, args=("Masala", 3), name="Masala Chai Thread")
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 5), name="Ginger Chai Thread")

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()