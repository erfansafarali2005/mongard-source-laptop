import time

start = time.perf_counter()

def show(name):
    print(f'starting {name} ...')
    time.sleep(3) # in 3 seconds its downloading a video or converting it
    print(f'finishing {name} ...')
    
show('one')
show('two')    
    
    
end = time.perf_counter() 

print(f' task takes {round(end - start)} seconds')   # This is sequential tasks . one start after each other 2 3 seconds , while its wating cpu and thread is now doing anything
    