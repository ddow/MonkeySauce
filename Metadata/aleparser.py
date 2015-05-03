__author__ = 'Daniel Dow for PIX|System'

"Parses ALE metadata into indexed data structures."

from itertools import islice
from itertools import groupby


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

    def dicts(self, value=None):
        """given any value for one item in the ALE, returns a list
         of dicts of all of the key/value pairs for each item that
         contains the value.
        """
        if value is None:
            return [dict(zip(self.keys, line)) for line in self.data]
        return [dict(zip(self.keys, line)) for line in self.data if value in line]

    def get_items(self, value, key=None):
        """Returns list of item returned by dict of value.  Key signifies
         metadata values returned in list.  If no key is given, all
         metadata for each item is returned.
        """
        if key is None:
            return self.dicts(value)
        else:
            items = self.dicts(value)
            return [item[key] for item in items]

    def slice(self, start=0, stop=None, step=1):
        """retruns opbject containing slice of Ale_parser object.
        """
        if not isinstance(start, int):
            for item in self.data:
                if start in item:
                    start = self.data.index(item)
            if not isinstance(start, int):
                raise ValueError('The start value you entered does not exist in this ALE.')
        if stop is None: stop = len(self.data)
        if not isinstance(stop, int):
            for item in self.data:
                if stop in item:
                    stop = self.data.index(item)
            if not isinstance(stop, int):
                raise ValueError('The stop value you entered does not exist in this ALE.')
        if stop < start and step > 1:
            raise ValueError('You have selected a stop value that is earlier than your start value and your step value is positive.')
        result = islice(self.data, start, stop, step)
        return result

    def group(self, key=None):

        if key is None:
            key = self.keys[0]
        if key not in self.keys:
            raise ValueError('The key you entered does not exist in this ALE.')
        data = sorted(self.dicts(), key=lambda d: d.get(key))
        result = [list(g) for k, g in groupby(data)]
        print(result)
        return result


#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
