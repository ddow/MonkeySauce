__author__ = 'ddow'

def ulam(n):
    """Returns the next hailstone number after n.
    """

    # Replace the pass below with your own code.
    if n % 2 == 0:
        n = n//2
    else:
        n = n*3+1
    return(n)


def stones(seed):
    """Returns a list of the hailstone numbers starting from the given seed.

    For example:

    >>> stones(17)
    [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """

    # Replace the pass below with your own code.
    list = []
    while seed > 1:
        list = list + [seed]
        seed = ulam(seed)
    list = list + [seed]
    return list



def measure(seed):
    """ For a given seed, returns the biggest of the stones.

    """

    # Replace the pass below with your own code.
    height = 0
    for n in stones(seed):
        if n > height:
            height = n
    return height