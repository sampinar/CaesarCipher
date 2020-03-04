#!/usr/bin/env python3
# Exercise genPrimes from edx week5 OOP
# As you call 'g' below, it will generate prime numbers starting from '2'. https://en.wikipedia.org/wiki/Prime_number

def genPrimes():
    y = 2

    while True:
        x = y // 2
        while x > 1:
            if y % x == 0:
                y += 1
                break
            x -= 1
        else:
            yield y
            y += 1


g = genPrimes()
pass


