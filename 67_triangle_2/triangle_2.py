"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle in the file
triangle.txt
"""
import numpy as np

a = open("triangle.txt", "r").read().split()
triangle = [int(i) for i in a]

n = 1
d = []
tmp = []
for i in triangle:
    tmp.append(i)
    if len(tmp) == n:
        d.append(tmp)
        tmp = []
        n += 1
d.reverse()
d = np.array([np.array(i) for i in d])
f = np.copy(d)

for i in range(1,len(d)):
    for j in range(len(d[i])):
        tmp = [d[i-1][j] if j<len(d[i-1]) else 0, d[i-1][j+1] if (j+1)>=0 else 0]
        d[i][j] += max(tmp)
        # print(d[i-1])
        # print(d[i],tmp,i,j)
for i in d:
    print(i)
        