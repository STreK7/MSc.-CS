import random
from timeit import default_timer as timer

#setting up random list
x=[]
n=2000
for i in range(n):
    x.append(random.randint(1000,10000))

print("Without Threading in range (1000, 10000)")
#timer start
start = timer()
arr = []
    
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return (a)


for i in range(0,len(x)):
    arr.append(fib(x[i]))
    #print("{0}: {1}".format(x[i], arr[i]))

print("Time taken %s seconds" % (timer() - start))



