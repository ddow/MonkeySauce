__author__ = 'Daniel Dow for PIX|System'

"Parses ALE metadata into indexed data structures."
PARSE_MODE_UNKNOWN = 0
PARSE_MODE_HEADER = 1
PARSE_MODE_COLUMNS = 2
PARSE_MODE_DATA = 3


class Ale_parser:
    """This class parses ALEs and defines methods for reading metadata from them.
    """
    def __init__(self, file):
        """Data structures are self.keys and self.data.  The data structure
         self.keys is a list of the keys from the ALE.  The data structure
         self.data is a list of the items in the ALE containing a list of
         the metadata values for the item.
        """
        self.data = []
        parse_mode = PARSE_MODE_UNKNOWN
        for line in open(file, 'r'):
            # Figure out if we should change our parse mode
            if line == 'Column\n':
                parse_mode = PARSE_MODE_COLUMNS
                continue
            elif line == 'Data\n':
                parse_mode = PARSE_MODE_DATA
                continue
            # Parse the data into keys or a list of items
            if parse_mode == PARSE_MODE_COLUMNS:
                self.keys = line.strip().split('\t')
                parse_mode = PARSE_MODE_UNKNOWN
                continue
            elif parse_mode == PARSE_MODE_DATA:
                item = line.strip().split('\t')
                self.data.append(item)
                continue

    def dicts(self, value):
        """given any value for one item in the ALE, returns a list
         of dicts of all of the key/value pairs for each item that
         contains the value.
        """
        return [dict(zip(self.keys, line)) for line in self.data if value in line]

    def get_items(self, value, key=None):
        """Returns list of item returned by dict of value.  Key signifies
         metadata values returned in list.  If no key is given, all
         metadata for each item is returned.
        """
        if key == None:
            return self.dicts(value)
        else:
            items = self.dicts(value)
            return [item[key] for item in items]