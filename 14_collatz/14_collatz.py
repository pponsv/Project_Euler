"""
Which starting number, under one million, produces the longest collatz
chain?
"""

def l_collatz(n,arr=[0,1]):
    l = 1
    if n<len(arr):
        l = arr[n]
    if n%2 == 0:
        if n//2 <= len(arr)-1:
            l += arr[n//2]
        else:
            l += l_collatz(n//2,arr)
    elif n%2 != 0:
        l += l_collatz(3*n+1,arr)
    return l



def collatz_max(n,arr=[0,1]):
    len_max = 0
    l = 0
    for i in range(2,n):
        if i % 2 == 0:
            arr.append(arr[i//2] + 1)
        elif i % 2 != 0:
            arr.append(l_collatz(i,arr))
    # print(([i,j] for i,j in enumerate(arr)))
    return arr.index(max(arr))


print(collatz_max(1000002))
"""
Tal vez habría sido mejor usar un diccionario
"""
