"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""
import numpy as np


def sum_divisors(n):
    suma = 0
    for i in range(1, int(np.sqrt(n))+1):
        if not n % i:
            suma += i + (0 if (i == 1 or i == np.sqrt(n)) else n/i)
    return suma


def isabundant(n):
    return sum_divisors(n) > n


abundants = np.array([], dtype=int)
for n in range(1, 28124):
    if isabundant(n):
        abundants = np.append(abundants, n)

max_num = 28124
numbers = list(range(0, max_num))
for i in abundants[:]:
    for j in abundants[abundants < max_num-i]:
        numbers[i+j] = 0

print(sum(numbers))
