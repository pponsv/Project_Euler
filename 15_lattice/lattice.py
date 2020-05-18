"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import numpy as np
size = 20
array = np.zeros((size+1,size+1),dtype=int)
array[0,:] = 1
array[:,0] = 1
for i in range(1,size+1):
    for j in range(1,size+1):
        array[i,j] += array[i-1,j] + array[i,j-1]
# print(array[19,19])
print(array[20,20])
