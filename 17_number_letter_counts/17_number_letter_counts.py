"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?
"""
import math

def ord(n):
    return math.floor(math.log10(n))

def numname(n):
    name = ''
    if ord(n) == 0:
        name += (units[n])
    elif ord(n) == 1:
        if n<20:
            name += (dec[n])
        else:
            name += (dec[10*(n//10)])
            rem = n%10
            if rem != 0:
                name += (numname(n%10))
    elif ord(n) == 2:
        name+=(units[n//100])
        name+=(ext[100])
        rem = n%100
        if rem != 0:
            name+='and'
            name+=(numname(n-100*(n//100)))
    elif ord(n) == 3:
        name+=(ext[1000])
    return name


units = {}
dec = {}
ext = {}

units[1] = 'one'
units[2] = 'two'
units[3] = 'three'
units[4] = 'four'
units[5] = 'five'
units[6] = 'six'
units[7] = 'seven'
units[8] = 'eight'
units[9] = 'nine'
units[0] = ''
dec[10] = 'ten'
dec[11] = 'eleven'
dec[12] = 'twelve'
dec[13] = 'thirteen'
dec[14] = 'fourteen'
dec[15] = 'fifteen'
dec[16] = 'sixteen'
dec[17] = 'seventeen'
dec[18] = 'eighteen'
dec[19] = 'nineteen'
dec[20] = 'twenty'

dec[30] = 'thirty'
dec[40] = 'forty'
dec[50] = 'fifty'
dec[60] = 'sixty'
dec[70] = 'seventy'
dec[80] = 'eighty'
dec[90] = 'ninety'

ext[100] = 'hundred'
ext[1000] = 'onethousand'

# n = 27
# print(numname(n))
# print(len(numname(n)))
names = ''
for n in range(1,1001):
    print(n)
    print(numname(n))
    names += numname(n)
print(len(names))
