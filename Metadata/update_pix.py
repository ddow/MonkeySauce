__author__ = 'ddow'

import os
import base64
from collections import OrderedDict
import getpass
from pix import PIXClient, PIXError, PIXItem, PIXAPIError
import aleparser

HOST = 'project.pixsystem.com'
APP_KEY = '7cc84b61-b42f-4477-a590-2d48f14ada27'
PROJECT_ID = 1207
USERNAME = 'pix_dan' #raw_input('Please enter your PIX username: ')
CLIENT = PIXClient(APP_KEY, HOST)


try:
    PASSWORD = os.environ['PIX_PASSWORD']
except KeyError:
    PASSWORD = 'TigAssBitties12!'

try:
    PASSWORD = base64.b64decode(PASSWORD)
except TypeError:
    PASSWORD = PASSWORD


def pix_login():
    try:
        CLIENT.login(USERNAME, PASSWORD, PROJECT_ID)
    except PIXAPIError as e:
        print 'Error connecting to PIX on {0}: {1}'.format(HOST, e.msg)
    else:
        print 'Connected to PIX on {0} as {1} (project {2})'.format(
            HOST, USERNAME, PROJECT_ID)


def pix_query(field, value, comp, sort=''):
    result = CLIENT.single_query(field, value, comp, sort)
    items = list(result)
    for item in items:
        i = result[item]
        if i.class_id != 22:
            result.pop(item)
    return result


def pix_update_metadata(file):
    ale_items = aleparser.AleParser(file)
    pix_items = pix_query('attr_key', 'Update', '!=')
    pix_items_values = list(pix_items.values())
    for pix_item in pix_items_values:
        value = pix_item.name
        item_id = pix_item.pixid
        item_dict = {}
        item_dict.update({'pixid':item_id})
        metadata = aleparser.AleParser.get_items(ale_items, value)
        item_dict.update({'metadata':metadata})
        print(item_dict)



        """
        for ale_item in ale:
            print(ale_item)
            if pix_item.name in ale_item:
                CLIENT.replace_attributes(pix_items[item], attributes)
"""










pix_login()
pix_update_metadata('test.ALE')