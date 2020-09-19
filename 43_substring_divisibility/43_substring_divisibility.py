"""
Find all 0-9 pandigital numbers whose substrings are recurrently divisible by
the first prime numbers
"""
from itertools import permutations
import time

t0 = time.time()

pandigitals = permutations([1,2,3,4,5,6,7,8,9,0])
primes = [2,3,5,7,11,13,17]

def lts(permutation):
    num = ''
    for i in permutation:
        num += str(i)
    return num

def condition(permutation):
    if permutation[0] == 0: return 0
    num = lts(permutation)
    # for i in range(6,-1,-1):
    for i in range(7):
        mod = int(num[i+1:i+4])%primes[i]
        # print(mod,i,int(num[i+1:i+4]),primes[i])
        if mod != 0:
            # print(mod)
            return 0
    return 1
total = 0

# print(condition('1406357189'))

for i in pandigitals:
    if condition(i):
        total += int(lts(i))
print(total)
print(time.time() - t0)
