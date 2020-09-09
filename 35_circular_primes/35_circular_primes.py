"""
How many circular primes are there below one million?
"""
import math

def rotation(n):
    order = math.floor(math.log10(n))
    nums = [n]
    for i in range(order):
        tmp = 10*n - (n//(10**order))*(10**(order+1)) + n//(10**order)
        nums.append(tmp)
        n = tmp
    return nums

a = [i for i in range(2,1_000_001)]
for i in a:
    if i != 0:
        temp = i+i
        while temp < 1_000_001:
            # print(temp,a[temp-2])
            a[temp-2] = 0
            temp = temp + i

b = [i for i in a if i != 0]
B = set(b)
total = 0
for i in b:
    nums = rotation(i)
    n = 0
    for j in nums:
        if j in B:
            n += 1
    if n == len(nums):
        print(nums)
        total += 1

print(total)


