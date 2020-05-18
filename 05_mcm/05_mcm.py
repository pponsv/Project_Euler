"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""
from math import log, floor


def check_prime(n):
    for i in range(2, n):
        if not n % i:
            return 0
            break
    return 1


def primes_to(n):
    primes = []
    for i in range(2, n+1):
        if check_prime(i):
            primes.append(i)
    return primes


def mcm(max_n):
    primes = primes_to(max_n)
    mcm = 1
    for i in primes:
        n = floor(log(max_n, i))
        mcm = mcm*i**n
    return mcm


n_max = 10
print(mcm(n_max))
