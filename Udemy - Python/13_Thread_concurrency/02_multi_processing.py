from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing process.")
    time.sleep(3)
    print(f"End of {name} chai brewing process.")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",)) 
        for i in range(3)
    ]

    # Start all chai brewing processes
    for p in chai_makers:
        p.start()

    # wait for all chai brewing processes to finish
    for p in chai_makers:
        p.join()