"""
Find the sum of the only eleven primes that are truncatable from left to right
and right to left
"""
import math

def truncate_left(n):
    order = math.floor(math.log10(n))
    return n - (n//10**order)*10**order

def truncate_right(n):
    return n//10

range_primes = 1000000
nums = [i for i in range(2,range_primes)]
for i in nums:
    if i != 0:
        temp = i+i
        while temp < range_primes:
            # print(temp,a[temp-2])
            nums[temp-2] = 0
            temp = temp + i

primes = [i for i in nums if i != 0]
primes_set = set(primes)
primes_truncatable = set([2,3,5,7])

for i in primes:
    a = i
    b = i
    n = 0
    while a > 10:
        a = truncate_left(a)
        b = truncate_right(b)
        if (a not in primes_set) or (b not in primes_set):
            n = 1
            break
    if n == 0:
        primes_truncatable.add(i)
print(sorted(primes_truncatable))
print(sum(primes_truncatable) -17)


# def truncations(n):
#     A, B = [n], [n]
#     a = n
#     b = n
#     while a > 10:
#         a = truncate_right(a)
#         b = truncate_left(b)
#         A.append(a)
#         B.append(b)
#     return [A,B]
