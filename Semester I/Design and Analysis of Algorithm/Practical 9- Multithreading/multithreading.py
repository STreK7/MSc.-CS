import queue, threading, random
from timeit import default_timer as timer

#setting up random list
x=[]
n=200
for i in range(n):
    x.append(random.randint(1000,10000))
    
print("With Threading in range (1000, 10000)")

#timer start
start = timer()
q = queue.Queue()


def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    q.put((n, a))
    return

for i in x:
    t = threading.Thread(target=fib, args = (i,))
    t.daemon = True
    t.start()

while not q.empty():
    n, f = q.get()
    #print ("{0}: {1}".format(n, f))

    
print("Time taken %s seconds" % (timer() - start))
