"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""
import numpy as np
import time
from itertools import permutations

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
t = time.time()
for i in permutations('7654321'):
    i = int(''.join(i))
    if is_prime(i):
        print(i)
        break
print(time.time() - t)
