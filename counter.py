""" A program that stores and updates a counter using a Python pickle file"""

import os
from os.path import exists
import sys
from pickle import dump, load


def update_counter(file_name, reset=False):
    """Update a counter stored in the file 'file_name'.

    A new counter will be created and initialized to 1 if none exists or if the
    reset True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    Parameters
    ----------
    file_name: str
        The file that stores the counter to be incremented.  If the file
        doesn't exist, a counter is created and initialized to 1.
    reset: bool
        True if the counter in the file should be reset.

    Returns
    -------
    int
        The new counter value

    Examples
    --------
    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    if os.path.exists(file_name) and reset==False:
        f = open(file_name, 'r')
        counter = f.readline()
        counter = int(counter[9:].strip())+1
        f = open(file_name, 'w')
        f.write('counter: %d' % counter)
        print(counter)
    else:
        f = open(file_name, 'w')
        counter = 1
        f.write('counter: %d' % counter)
        print(counter)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is {}".format(update_counter(sys.argv[1])))
