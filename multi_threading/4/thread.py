import time
from threading import Thread
import sys

# Daemon has conflict with join !!!!

start = time.perf_counter()

def show(name):
    print(f'starting {name} ...')
    time.sleep(3)
    print(f'finishing {name} ...')
    
t1 = Thread(target=show , args=('name 1',),daemon=False)
t2 = Thread(target=show , args=('name 2',),daemon=False)
t1.start()
t2.start()   

# if daemon false : which app riches the sys.exit , the app (won't exit) why -> threads always prevent exiting the app while running a task
# 
# but if you set the daemon True , it will exists the code while running the tasks because we can't use join 
# 
# if you use join with daemon app runs like daemon false , it will run and finishs the task and then the app ends
# 
# !!!! never change the daemon after start , it will break the app 
 
    
end = time.perf_counter() 

print(f' task takes {round(end - start)} seconds')   

sys.exit()
    