import timeit
import random
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    


SETUP_CODE = '''
from __main__ import insertion_sort
import random
'''

TEST_CODE = '''
arr=[]
for i in range (1,100000):
    n = random.randint(0,1000)
    arr.append(n)
insertion_sort(arr)'''

times = timeit.timeit(setup = SETUP_CODE,
                      stmt = TEST_CODE,
                      number = 1)

print(times)      
