#!/usr/bin/env python3
"""
Interactive script.
The user is asked repeatedly for an integer.
Hits return to quit.
"""

GREETING = 'Go Multiply!'
PROMPT = 'NUmber please: '
GOODBYE = 'Bye.  Thank you for using multscript'

print(GREETING)

product = 1

#Infinite loop, unless we break out.

while True:

    s = input(PROMPT)
    s = s.strip()

    if not s:
        print(GOODBYE)
        break

    if not s.isdigit():
        print('This is a multiplication script, you stupid moron!  Enter a number, asshole!')
        continue

    n = int(s)

    product = n * product
    print('Product so far: ', product)