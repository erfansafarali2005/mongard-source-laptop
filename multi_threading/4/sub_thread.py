import time
from threading import Thread

start = time.perf_counter()

def show(name , delay):
    print(f'starting {name} ...')
    time.sleep(delay)
    print(f'finishing {name} ...')
    

class ShowThread(Thread):
    def __init__(self , name , delay , *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.name = name 
        self.delay = delay

    def run(self):
        show(self.name , self.delay)

t1 = ShowThread('erfan' , 1 , daemon=True)

t1.start()

# t1.joint()

end = time.perf_counter() 

print(f' task takes {round(end - start)} seconds')  
    