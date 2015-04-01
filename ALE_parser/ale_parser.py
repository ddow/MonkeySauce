__author__ = 'Daniel Dow for PIX|System'

__doc__ = """
This program takes an ALE and outputs a file
containing a sigle dictionary for each item.
"""

from get_keys import getkeys

ALE = input('What ALE would you like to parse? ')   #Get the ALE to parse from the user

ALE = ALE + ".ALE"

KEYS = ()                                           #Create an empty tuple to hold the keys

OUTFILE = 'output.txt'                              #For now, use this file for output

output = open(OUTFILE, 'w')                         #Open the output file to write to

with open(ALE,'r') as ale:                          #Open the file to read from
    for item in ale:
        """
        Get rid of headers by ignoring lines less than 40 characters long.
        Also, skip blank lines between column headers and clip metadata.
        """
        if len(item) < 40:
            continue
        elif len(KEYS) == 0:
            """
            the first column we come to that is longer than 40 characters
            will be the column headers.  Use them as keys.
            """
            KEYS = item.split('\t')
            continue
        values = item.split('\t')
        """
        All the lines that are left will be metadata for each clip in the
        ALE.
        """
        metadata = str(list(zip(KEYS,values)))      #Turn each item into a string for output
        output.write(metadata + '\n')
