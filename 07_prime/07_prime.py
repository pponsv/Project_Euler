"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""
import numpy as np

a = np.asarray(list(range(2, 200000)))
primes = []
while len(primes) < 10001:
    if a.size == 0:
        print("not enough range")
        break
    i = a[0]
    a = a[((a % i != 0))]
    primes.append(i)
print(primes[-1])
