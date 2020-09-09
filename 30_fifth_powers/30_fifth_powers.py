"""
Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

import numpy as np
from itertools import permutations

def sum_power(n):
    n_str = str(n)
    suma = 0
    for i in n_str:
        suma += int(i)**5
    return suma

def list_to_str(lista):
    s = ''
    for i in lista:
        s += i
    return int(s)

items = '0123456789'
n = 0
for i in range(10,1000000):
    if i == sum_power(i):
        print(i,'   ',sum_power(i))
        n += i
print(n)

