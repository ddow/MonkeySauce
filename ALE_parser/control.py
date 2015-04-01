__author__ = 'Daniel Dow for PIX|System'

__doc__ = """
This program takes an ALE and outputs a file
containing a single dictionary for each item.
"""

from get_keys import getkeys

from get_values import getvalues

from file_updater import updater

ALE = input('What ALE would you like to parse? ')   #Get the ALE to parse from the user

if ALE[::-3].lower() != 'ale':

    ALE = ALE + ".ALE"

NAME = input('What column contains the current PIX name for the file? ')

KEYS = ()                                           #Create an empty tuple to hold the keys

OUTFILE = 'output.txt'                              #For now, use this file for output

output = open(OUTFILE, 'w')                         #Open the output file to write to

check = ''                                          #In case we don't like the column they choose...

with open(ALE,'r') as ale:                          #Open the file to read from
    for item in ale:
        """
        Get rid of headers by ignoring lines less than 40 characters long.
        Also, skip blank lines between column headers and clip metadata.
        """
        if len(item.strip()) < 40:
            continue
        elif len(KEYS) == 0:
            """
            the first column we come to that is longer than 40 characters
            will be the column headers.  Use them as keys.
            """
            KEYS = getkeys(item)
            continue
        values = getvalues(item)
        zip_metadata = zip(KEYS,values)
        metadata = dict(list(zip_metadata))
        metadata_string_dict = metadata[NAME]
        if '.mov' not in metadata_string_dict and check != 'done':
            print('This column does not look like it contains a valid PIX filename')
            so_what = input('Are you sure you wish to use this column (y/n)? ' )
            if so_what == 'y':
                check = 'done'
                pass
            else:
                print('operation cancelled!')
                break
        metadata = {metadata_string_dict:metadata}
        updater(metadata)
#        print(metadata)