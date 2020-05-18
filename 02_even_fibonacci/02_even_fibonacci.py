"""
Eachnew term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


def fibonacci_to_mf(MAX_FIB):
    fib = [1, 1]
    while fib[-1] < MAX_FIB:
        fib.append(fib[-1] + fib[-2])
    fib.pop(-1)
    return fib


MAX_FIB = 4e6
fib_calc = fibonacci_to_mf(MAX_FIB)

suma_fib = 0
for i in fib_calc:
    if i % 2:
        suma_fib += i

print(suma_fib)
