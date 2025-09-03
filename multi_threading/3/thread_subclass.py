import time
from threading import Thread

start = time.perf_counter()

def show(name , delay):
    print(f'starting {name} ...')
    time.sleep(delay)
    print(f'finishing {name} ...')
    
class ShowThread(Thread):
    def __init__(self , name , delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name , self.delay)

t1 = ShowThread('erfan' , 1)
t2 = ShowThread('amir' , 2) 

t1.start()
t2.start()

t1.join()
t2.join()
    
end = time.perf_counter() 

print(f' task takes {round(end - start)} seconds')  
    