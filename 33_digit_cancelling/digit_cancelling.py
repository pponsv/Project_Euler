"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

import numpy as np

nums = '123456789'
num = []
den = []
for i in range(11,100):
    for j in range(10,i):
        i_n = [i//10,i%10]
        j_n = [j//10,j%10]
        for k in i_n:
            # print('I    ',i_n,k)
            if (k in j_n) & (k != 0):
                # print('J    ',j_n,k)
                i_n.remove(k)
                I = i_n[0]
                j_n.remove(k)
                J = j_n[0]
                # print(I,J)
                if (I != 0):
                    if (J/I == j/i):
                        num.append(J)
                        den.append(I)
                        print(j,'   ',i,'   ',J,'   ',I,'   ',j/i, J/I)

d_prod = 1
n_prod = 1
for i in den:
    d_prod *= i
for i in num:
    n_prod *= i
print(n_prod,d_prod,d_prod/n_prod)
