"""
The sum of the squares of the first ten natural numbers is,

1**2+2**2+...+10**2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)**2=552=3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
n = 100
nums = list(range(1, n+1))
sum_sq = 0

for i in nums:
    sum_sq += i**2
sq_sum = sum(nums)**2
print(sq_sum - sum_sq)
