"""
Find the pair of pentagonal numbers for which their sum and difference are
pentagonal and the absolute value of the difference, D = |p_i - p_j|, is
minimised
"""
import math

def pn(n):
    return int(n*(3*n-1)/2)

def np(a):
    n = 1/6 + math.sqrt(24*a + 1)/6
    if n.is_integer():
        return int(n)
    else:
        return 0

lim = 1000
end = False
i = 0
while end == False:
    i += 1
    for j in range(1,i):
        a = np(pn(i) - pn(j))
        b = np(pn(i) + pn(j))
        # print(i,j,' a = ',a,'    b = ',b)
        if a:
            if b:
                print(a,b,i,j,pn(i),pn(j),pn(i)-pn(j))
                end = True

