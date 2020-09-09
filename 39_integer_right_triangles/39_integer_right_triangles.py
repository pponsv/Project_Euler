"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math
import time
t0 = time.time()

def hyp(a,b):
    c = math.sqrt(a**2 + b**2)
    if c.is_integer():
        return int(c)
    else:
        return 0

freq = {}
for a in range(2,500):
    for b in range(1,a):
        c = hyp(a,b)
        if c:
            p = a+b+c
            if p > 1000:
                break
            # print(p,a,b,c)
            if p in freq.keys():
                freq[p] += 1
            else:
                freq[p] = 1

print(max(freq,key=freq.get), freq[max(freq,key=freq.get)])

print(time.time() - t0)
