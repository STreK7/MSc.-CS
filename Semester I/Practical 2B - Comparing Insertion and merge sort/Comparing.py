import matplotlib.pyplot as plt
import numpy as np
from insertionsort import insertion_sort
from mergesort import mergeSort,merge
import timeit
import random

SETUP_CODE = '''
from __main__ import insertion_sort
import random
'''
x = [0, 100 , 200 , 400 ,800]
y = []

#0
TEST_CODE = '''
arr=[]
for i in range (1,0):
    n = random.randint(0,100)
    arr.append(n)
insertion_sort(arr)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)
y.append(times)


#100
TEST_CODE = '''
arr=[]
for i in range (1,100):
    n = random.randint(0,100)
    arr.append(n)
insertion_sort(arr)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)
y.append(times)
#200
TEST_CODE = '''
arr=[]
for i in range (1,200):
    n = random.randint(0,100)
    arr.append(n)
insertion_sort(arr)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)
y.append(times)

#400
TEST_CODE = '''
arr=[]
for i in range (1,400):
    n = random.randint(0,100)
    arr.append(n)
insertion_sort(arr)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)
y.append(times)

#800
TEST_CODE = '''
arr=[]
for i in range (1,800):
    n = random.randint(0,100)
    arr.append(n)
insertion_sort(arr)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)
y.append(times)

print(y)

# merge sort

SETUP_CODE = '''
from __main__ import mergeSort,merge
import random
'''

y1 = []
#0
TEST_CODE = '''
arr=[]
for i in range (1,0):
    n = random.randint(0,100)
    arr.append(n)
mergeSort(arr, 0, len(arr)-1)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)

y1.append(times)

#100
TEST_CODE = '''
arr=[]
for i in range (1,100):
    n = random.randint(0,100)
    arr.append(n)
mergeSort(arr, 0, len(arr)-1)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)

y1.append(times)
#200
TEST_CODE = '''
arr=[]
for i in range (1,200):
    n = random.randint(0,100)
    arr.append(n)
mergeSort(arr, 0, len(arr)-1)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)

y1.append(times)


#400
TEST_CODE = '''
arr=[]
for i in range (1,400):
    n = random.randint(0,100)
    arr.append(n)
mergeSort(arr, 0, len(arr)-1)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)

y1.append(times)

#800
TEST_CODE = '''
arr=[]
for i in range (1,800):
    n = random.randint(0,100)
    arr.append(n)
mergeSort(arr, 0, len(arr)-1)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)

y1.append(times)

# second plot with x1 and y1 data
print(y1)
# first plot with X and Y data
plt.plot(x, y, label="Insertion sort n^2")
plt.plot(x, y1, label="Merge sort n.log n")
  
plt.xlabel("Input size")
plt.ylabel("Time taken")
plt.title('Comparing Insertion sort and Merge sort')
plt.legend()
plt.show()
