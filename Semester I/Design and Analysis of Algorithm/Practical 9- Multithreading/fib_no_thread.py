import time
import sys
sys.setrecursionlimit(10000)
print("Without Threading")

start_time = time.time()

    
def fib(x):
    if(x < 1):
        return 0
    return x+fib(x-1)


print(fib(2100))
print("Time taken %s seconds" % (time.time() - start_time))
