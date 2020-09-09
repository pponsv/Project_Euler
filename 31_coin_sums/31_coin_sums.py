"""
How many different ways can £2 be made using any number of coins?
"""

import numpy as np

def possible_arrangements(n,value):
    pos_val = []
    for i in range(n//value+1):
        pos_val.append(i)
    return pos_val

def n_arrangements(coins,total):
    k = possible_arrangements(total,coins[0])
    n = 0
    if (len(coins) == 1):
        if (not total%coins[0]):
            n = 1
            return n
        else:
            n = 0
            return n
    else:
        for i in k:
            tmp = total-i*coins[0]
            tcoins = coins[1::]
            n += n_arrangements(tcoins,tmp)
    return n

coins = [1, 2, 5, 10, 20, 50, 100, 200]

# coins = [1,2,5]
coins.reverse()
print(n_arrangements(coins,200))
