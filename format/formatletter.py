__author__ = 'ddow'

# We explore three ways of filling in the data into a form letter.

name, units, item, unitprice = 'Customer', 20, 'turtles', 40.2
total = units * unitprice
signature = 'Sarah Palindrone'

TEMPLATE1 = """
Dear {},

Thanks for your order of {} {} at a unit price of {}.
Your total bill will be {} payable at your convenience.
You may order more {} any time.

Downtown Billing,

{}
"""

LetterA = TEMPLATE1.format(name, units, item, unitprice, total, item, signature)

# Using keyword.

TEMPLATE2 = """
Dear {name:},

Thanks for your order of {units:} {item:} at a unit price {unitprice:}.

Your total bill will be {total:}, payable at your convenience.

You may order more {item:} any time.

Downtown Billing,

{signed:}
----------------------------------------------------------------------
"""

LetterB = TEMPLATE2.format(item='Turtles', units=20, name='Customer', unitprice=40.2,
                           signed='Sara Palindrome', total=20*40.2)


# dictionary

d = dict()
d['name'] = 'Customer'
d['item'] = 'pythons'
d['units'] = 20
d['unitprice'] = 120.50
d['signed'] = 'Sarah Palindrome'
d['total'] = d['units'] * d['unitprice']

LetterC = TEMPLATE2.format(**d)

print(LetterA)

print(LetterB)

print(LetterC)