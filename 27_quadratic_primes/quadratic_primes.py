"""
Find the product of the coefficients "a" and "b" for the quadratic expression

n^2 + an + b = p_n

that produce the greatest amount of primes for consecutive values of n,
starting from n=0
"""

import numpy as np

def isprime(p):
    if p<2:
        return 0
    for i in range(2,p//2+1):
        if not p%i:
            return 0
    return 1

def pn(a,b,n):
    return n**2 + a*n + b

imax = 0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        n = 0
        while isprime(pn(a,b,n)):
            # print(a,b,n,'   ',pn(a,b,n))
            n += 1
        if n > imax:
            imax = n
            coef = [a,b,a*b]
print(imax,'    ',coef)
