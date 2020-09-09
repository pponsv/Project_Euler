"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.
"""

import numpy as np
from itertools import permutations
def is_pandigital(a,b='',c=''):
    total = str(a) + str(b) + str(c)
    print(sorted(total))
    if sorted(total) == sorted('123456789'):
        return 1
    else:
        return 0

def leftover_numbers(a,b=''):
    total = str(a) + str(b)
    if len(total) != len(np.unique(np.asarray(total))[0]):
        return ''
    nums = '123456789'
    for i in total:
        nums = nums.replace(i,'')
    return nums

nums = '123456789'

prods = []
for i in range(1,6):
    for a in permutations(nums,i):
        a = ''.join(a)
        tmp = leftover_numbers(a)
        for j in range(1,6-i):
             for b in permutations(tmp,j):
                b = ''.join(b)
                c = leftover_numbers(a,b)
                for k in permutations(c):
                    k = ''.join(k)
                    if int(a)*int(b) == int(k):
                        print(a,' * ',b,' = ',k)
                        prods.append(k)

prods = np.unique(np.asarray(prods))
print(len(prods))
print(prods)
tot = 0
for i in prods:
    tot += int(i)
print(tot)
