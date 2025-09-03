import time
from threading import Thread

start = time.perf_counter()

def show(name):
    print(f'starting {name} ...')
    time.sleep(3) # in 3 seconds its downloading a video or converting it
    print(f'finishing {name} ...')
    
t1 = Thread(target=show , args=('name 1',))
t2 = Thread(target=show , args=('name 2',))
t1.start()
t2.start()   # you must start the task | we must block the code to prevent the threading to continue going to the next line of the codes

t1.join()
t2.join() # now here the code will be blocked here until the t1 and t2 are executed
    
# if you dont use join : the threads wil be started and also while its working (sleep) the time will be printed    
# if you just use join for t1 , the t2 and printing of the time will be executed togheter
# now 2 tasks are being started togheter and only taks 3 seconds     
    
end = time.perf_counter() 

print(f' task takes {round(end - start)} seconds')   
    