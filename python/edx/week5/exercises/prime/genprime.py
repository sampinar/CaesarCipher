#!/usr/bin/env python3

def genPrimes(number):
    ans = []
    factor = 2
    #ans.append(factor)  # append the first factor '2'

    for i in range(2, number+1):
        if not ans:
            ans.append(factor)
            #next

        elif (i % factor) != 0:
            ans.append(i)
    yield ans

g = genPrimes(20)
pass


