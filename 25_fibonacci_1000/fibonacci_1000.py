"""
The 12th term, of the fibonacci sequence, F12, is the first term to contain
three digits.

What is the index of the first term in the Fibonacci sequence to contain
1000 digits?
"""


def fi(n):
    init = [1,1]
    N = 0
    for i in range(2,n):
        N = sum(init)
        init[0] = init[1]
        init[1] = N
    return N


def lstr(n):
    return len(str(n))

N = 10
while lstr(fi(N))<1000:
    N *= 2
    print(N)

while lstr(fi(N))>999:
    N -= 1
    print(N)
    if lstr(fi(N)) == 999:
        break
print(N+1)
