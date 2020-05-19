"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

Evaluate the sum of all the amicable numbers under 10000.
"""
import numpy as np

def sum_divisors(n):
    suma = 0
    for i in range(1,int(np.sqrt(n))+1):
        if not n%i:
            suma += i + (0 if (i==1 or i == np.sqrt(n)) else n/i)
            # print(suma, i, n/i, (i==0 or i == np.sqrt(n)))
    return suma

suma = 0
for i in range(1,10000):
    st = sum_divisors(i)
    if ((sum_divisors(st) == i) & (st != i)):
        suma += i

print(suma)

