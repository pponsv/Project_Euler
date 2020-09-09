"""
Find the sum of all numbers which are equal to the sum of the factorial of
their digits.
"""
import math
def factorial_sum(n):
    fact = 0
    while n>=1:
        # print(n, fact)
        fact += math.factorial(n%10)
        n = n//10
    return fact
tmp = 0
for i in range(3,10_000_000):
    if i == factorial_sum(i):
        tmp += i
print(tmp)
