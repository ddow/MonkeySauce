__author__ = 'Daniel Dow for PIX|System'

__doc__ = """
This function grabs the column headers from an ALE and stores them as keys.
"""

def getkeys(headers):
    keys = headers.split('\t')
    return(keys)
