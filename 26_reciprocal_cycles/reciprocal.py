"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""


def rem_vector(n):
    # print('{0:.30f}'.format(1/n))
    r = [1]
    d = [0]
    while r[-1] != 0:
        tmp = 10 * (r[-1]%n)
        # print(r[-1], r[-1]%n, tmp, r)
        if not tmp in r:
            r.append(tmp)
            d.append(tmp//n)
        else:
            return r
    return r
    # print(r)

l = 0
for i in range(2,1001):
    tmp = rem_vector(i)
    if len(tmp)>l:
        l = len(tmp)
        N = i
print(N)

# print(rem_vector(97), 10%7)
