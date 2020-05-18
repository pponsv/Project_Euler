"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

----------------------------------------------------------

Dos formas de hacerlo, ambas por fuerza bruta.

En la primera se calculan todos los múltiplos palíndromes de dos
numeros < 1000, y se encuentra su máximo. Es algo más lenta.

En la segunda, se parte de 999*999 y, bajando, se comprueba si el número es
palíndromo, y en caso afirmativo si tiene dos divisores menores que 1000
"""
import time


def check_palindrome(n):
    n_arr = str(n)
    if n_arr == n_arr[::-1]:
        return True
    else:
        return False


t1 = time.time()
palindromes = []
for i in reversed(range(1000)):
    for j in reversed(range(i, 1000)):
        if check_palindrome(i*j):
            palindromes.append(i*j)
print(time.time() - t1)
print(max(palindromes))


t2 = time.time()
i = 999*999
convergence = False
while convergence is False:
    i -= 1
    if check_palindrome(i):
        for j in reversed(range(1, 1000)):
            if ((not i % j) & (i/j < 1000)):
                print(i, i/j, j)
                convergence = True
                break

print(i)
print(time.time() - t2)
