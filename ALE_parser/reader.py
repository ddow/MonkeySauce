"""
This file strips out the junk at the top of an ALE, finds the column headers to create keys
 and creates dictionaries out of the values.
"""

from get_keys import getkeys

KEYS = ()

FILE = input('ALE? ',)

with open(FILE, 'r') as ale:
    for item in ale:
        if len(item) < 40:                  #Get rid of the junk at the top
            continue
        elif len(KEYS) == 0:                #First line with any length are the columns headers
            KEYS = item.split('\t')
            continue
        values = item.split('\t')           #All lines after that are values for individual shots
        clip_metadata = zip(KEYS,values)
for shot in clip_metadata:
    print(shot)