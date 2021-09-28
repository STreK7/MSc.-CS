import matplotlib.pyplot as plt
import numpy as np
import math

x = [ 0, 5, 10, 15, 20]
y=[0]
y1=[0]
for i in x:
    if i== 0:
        continue
    n = i*i
    y.append(n)
    z = i*(math.log(i,2))
    y1.append(z)


print(y)
print(y1)
plt.plot(x, y, label="Insertion sort n^2")
plt.plot(x, y1, label="Merge sort n.log n")
  
plt.xlabel("Input size")
plt.ylabel("Time taken")
plt.title('Comparing Insertion sort and Merge sort')
plt.legend()
plt.show()
