__author__ = 'ddow'

from Metadata import aleparser

def list2tdrow(data):
    """Returns a data row for a webpage html table.
    """
    lists = data
    line = '<tr>'
    for value in lists:
        if not value: value = 'blank'
        line += '<td>' + value.strip() + '</td>'
    line += '</tr>'
    return line

def list2throw(keys):
    """Returns a data headers for a webpage html table.
    """
    lists = keys
    headers = '<tr>'
    for item in lists:
        headers += '<th>' + item.strip() + '</th>'
    headers += '</tr>\n'
    return headers

def lists2table(ale):
    """
    """
    lists = aleparser.AleParser(ale)
    table = '<table>\n'
    table += list2throw(lists.keys)
    for item in lists.data:
        table += list2tdrow(item) + '\n'
    table += '</table>'
    return table

ALE = lists2table('204027.ALE')
print(ALE)