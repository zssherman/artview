"""
parser.py

Parse the input code from execution program.
"""

import argparse
import sys

# Get the version
# AG - python 3 decided it doesn't like scripts inside modules.
# I have read some posts about it and no one has a real solution.
# http://stackoverflow.com/questions/16981921/relative-imports-in-python-3
try:
    import version
except:
    from . import version

NAME = 'ARTview'
VERSION = version.version


def parse(argv):
    '''
    Parse the input command line.

    Parameters::
    ----------
    argv - string
        Input command line string.

    Notes::
    -----
    Returns directory and field for initialization.
    '''
    parser = argparse.ArgumentParser(
        description="Start ARTview - the ARM Radar Toolkit Viewer.")

    parser.add_argument('-v', '--version', action='version',
                        version='ARTview version %s' % (VERSION))

    # Directory argument now optional
    parser.add_argument('-d', '--directory', type=str,
                        help='directory to open', default='./')
    parser.add_argument('-f', '--field', type=str, help='Field to show',
                        default=None)
    parser.add_argument('-F', '--file', type=str, help='File to show',
                        default=None)
    parser.add_argument(
        '-s', '--script', type=str,
        help='Select from artview.scripts a script to execute', default=None)

    # Parse the args
    args = parser.parse_args(argv[1::])

    return args.script, args.directory, args.file, args.field
