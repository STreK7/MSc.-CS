from functools import wraps
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
    return arr


if __name__ == "__main__":
    arr=[]
    for i in range (1,10):
        n = random.randint(0,1000)
        arr.append(n)
    print(insertion_sort(arr))
