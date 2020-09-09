"""
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import numpy as np
import time

t0 = time.time()


def concatenation(N,n):
    conc = ''
    for i in range(1,n+1):
        conc += str(N*i)
    return int(conc)

def nine_concatenation(N):
    n = 1
    conc = ''
    while len(conc)<9:
        conc = str(concatenation(N,n))
        n += 1
    return int(conc) if len(conc) == 9 else 0

def is_pandigital(n):
    a = set('123456789')
    if (len(str(n)) == 9) & (set(str(n)) == a):
        return 1
    else:
        return 0

b = 0
for i in np.arange(1,10000):
    a = nine_concatenation(i)
    if is_pandigital(a):
        b = max(b,a)
print(b)
print(time.time() - t0)
