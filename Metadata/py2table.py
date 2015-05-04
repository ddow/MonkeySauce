__author__ = 'ddow'

from Metadata import aleparser

def list2tdrow(ale):
    """Returns a data row for a webpage html table.
    """
    lists = ale.data
    result = '<tr>'
    for item in lists:
        for value in item:
            result += '<td>' + value.strip() + '</td>'
        result += '\n'
    result += '</tr>'
    return result

def list2throw(ale):
    """Returns a data headers for a webpage html table.
    """
    lists = ale.keys
    result = '<tr>'
    for item in lists:
        result += '<th>' + item.strip() + '</th>'
    result += '</tr>\n'
    return result

def lists2table(ale):
    """
    """
    lists = aleparser.AleParser(ale)
    result = '<table>\n'
    result += list2throw(lists.keys) + '\n'
    for item in lists.data:
        result += list2tdrow(item) + '\n'
    result += '</table>'
    return result

ALE = lists2table('204027.ALE')
print(ALE)