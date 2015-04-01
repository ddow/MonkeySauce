__author__ = 'ddow'

"""
Notes on creating a form letter.
Continuing from almost the same file from last week.
This time, Dan was at the computer.
"""

# We explore three ways of filling data into a form letter.

name, units, item, unitprice = 'Customer', 20, 'turtles', 40.2
total = units * unitprice
signature = 'Sarah Palindrome'

TEMPLATE1 = """
Dear {},

Thanks for your order of {} {} at a unit price of {}.
Your total bill will be {}, payable at your convenience.
You may order more {} any time.

Downtown Billing,

{}
"""
LetterA = TEMPLATE1.format(name,units,item,unitprice,total,item,signature)

print(LetterA)

# NOTE THE FORMAT FOR {total:} It gives two decimals and uses commas for big numbers

# Using keywords

TEMPLATE2 = """
Dear {name:},

Thanks for your order of {units:} {item:} at a price of ${unitprice:0.02f}.

Your total will be ${total:0,.02f}, payable at your convenience.

You may order more {item:} any time.

Downtown Billing,

{signed:}
------------------------------------------------------------------------
"""


LetterB = TEMPLATE2.format(item='turtles', units=40, name='customer', unitprice=60.2, signed='Sara Palindrome',
                           total=units*unitprice)

print(LetterB)


# dictionary

d = dict()
d['name']='Customer'
d['item']='pythons'
d['units']=20
d['unitprice']=120.50
d['signed']='Sarah Palindrome'
d['total']=d['units']*d['unitprice']

LetterC = TEMPLATE2.format(**d)

print(LetterC)