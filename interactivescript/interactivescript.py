#!/usr/bin/env python3
"""
This is a python script.  Notice the very first line in this file.

It starts with #!

You can run it two different ways:

$python3 interactivescript

or make it executable and then run it.

chmod 755 interactivescript
./interactivescript
"""

prompt = 'Are you here? [Yn]: '

while True:

    answer = input(prompt)
    answer = answer.strip()

    if not answer or answer[0] in ['Y','y']:
        affirmed = True
        break

    if answer[0] in ['N', 'n']:
        affirmed = False
        break

print('Affirmative?', affirmed)