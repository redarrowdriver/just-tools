# Large files will read a directory from the top down and output files that are over or equal
# to a set file size. This is useful in auditing and scoping clients' servers for backup.

import os
import argparse

parser = argparse.ArgumentParser(description='Find fils that are over a set file size. Displayed in MBs.')
parser.add_argument('-d', '--dir', help='The directory to scan.')
parser.add_argument('-l', '--log', help='The location of the log file.')
parser.add_argument('-s', '--size', help='The large file size limit. Files equal to or larger than this size'
                                         ' will be found.')
args = parser.parse_args()
