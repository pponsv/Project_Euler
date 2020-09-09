"""
Find the last ten digits of the series:
    1**1 + 2**2 + 3**3 + ... + 1000**1000
"""

# Como python tiene soporte para enteros arbitrariamente grandes, es trivial:

import time
t0 = time.time()
a = 0
for i in range(1,1001):
  a += i**i
print(str(a)[-10:])
print(time.time() - t0)

# Corre en ~7 ms en mi portátil (i5 8300h)

