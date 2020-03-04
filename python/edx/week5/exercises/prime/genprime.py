#!/usr/bin/env python3

def genPrimes():
    ans = []
    prime = 2

    while True:
        x = prime // 2
        while x > 1:
            if prime % x == 0:
                break
            x -= 1
            prime += 1
        else:
            ans.append(i)
            yield i
            prime += 1


g = genPrimes()
pass


