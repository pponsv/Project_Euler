"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
El programa es caca caliente, revisar
"""


def g(x, n):
    return (x**2 + 1) % n


def gcd(a, b):
    while b != 0:
        rem = a % b
        a = b
        b = rem
    return a


def prime_factors(N):
    n = N
    x, y, d = 2, 2, 1
    factors = []
    itern = 0
    while True:
        x = g(x, N)
        y = g(g(y, N), N)
        d = gcd(abs(x-y), N)
        if (d > 1) & ((d not in factors) & (d != n)):
            factors.append(d)
            print(factors)
        N = N/d
        itern += 1
        if itern > 1e5:
            factors.append(N)
            break
    return factors


def producto(vec):
    prod = 1
    for i in vec:
        prod = prod*i
    return prod


N = 600851475143
factors = prime_factors(N)
print(producto(factors))
