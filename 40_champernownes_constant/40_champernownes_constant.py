"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

nums = [1, 10, 100, 1000, 10000, 100000, 1000000]

a = True
i = 0
n = 0
dn = 0
k = 1
while a == True:
# while n < 101:
    i += 1
    i_str = str(i)
    dn = len(str(i)) - 1
    n += 1
    # print(i,n,dn)
    if n <= nums[0] <=  n+dn:
        tmp = int(i_str[nums[0]-n])
        k *= tmp
        print(i,n,nums[0],tmp)
        nums.pop(0)
        if len(nums) == 0:
            a = False
    n += dn

print(k)
