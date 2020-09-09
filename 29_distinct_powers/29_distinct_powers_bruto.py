import numpy as np
import time

b = time.time()
a = []
n = 0
m = 101
for i in range(2,m):
    for j in range(2,m):
        tmp = i**j
        if not tmp in a:
            a.append(tmp)
            n += 1
print(time.time()-b,' s')
print(n)
