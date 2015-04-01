__author__ = 'Daniel Dow for PIX|System'

response = 'Updating {0}... '

def updater(item):
    item = str(item.keys())
    item = item.strip('dict_keys[]\'()')
    print(response.format(item))