import threading 
import queue
import time
import sys
sys.setrecursionlimit(10000)
print("With Threading")
start_time = time.time()

    
def fib(x, stop):
    if(x < stop):
        return 0
    #print(f"{threading.currentThread().getName()} value {x} \n")
    return x+fib(x-1, stop)


que = queue.Queue()
threads_list = list()
x = 2100
h1 = x
h2 = int(abs(x/2))
stop = h2+1
fib_thread1 = threading.Thread(target=lambda q, arg1: q.put(fib(arg1, stop)), args=(que, h1))
fib_thread1.start()
threads_list.append(fib_thread1)
fib_thread2 = threading.Thread(target=lambda q, arg1: q.put(fib(arg1, 0)), args=(que, h2))
fib_thread2.start()
threads_list.append(fib_thread2)

for t in threads_list:
    t.join()

total = 0
while not que.empty():
    result = que.get()
    total = total + result
print(total)


print("Time taken %s seconds" % (time.time() - start_time))
