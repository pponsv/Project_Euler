"""
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2
"""

def binary(n):
    return str(bin(n))[2:]

def is_palindrome(s):
    if s[::-1] == s:
        return 1
    else:
        return 0

s = 'aabaa'

suma = 0
for i in range(1_000_001):
    n_dec = str(i)
    n_bin = binary(i)
    if is_palindrome(n_dec) & is_palindrome(n_bin):
        print(n_dec,'   ',n_bin)
        suma += i
print(suma)
