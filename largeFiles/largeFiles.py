# Large files will read a directory from the top down and output files that are over or equal
# to a set file size. This is useful in auditing and scoping clients' servers for backup.

import os
import argparse

parser = argparse.ArgumentParser(description='Find fils that are over a set file size. Displayed in MBs.')
parser.add_argument('-d', '--dir', help='The directory to scan.')
parser.add_argument('-l', '--log', help='The location of the log file.', default='largeFiles.txt')
parser.add_argument('-s', '--size', help='The large file size limit. Files equal to or larger than this size'
                                         ' will be found.', default=100, type=int)
args = parser.parse_args()

print('RedArrowDriver\n\nLarge Files Version 0.1\nHelps find large files in a directory and its sub-dirs.\n\n')

# check to see if use supplied directory in args
if args.dir is None:
    args.dir = input(f'Enter a directory to scan: ')
    if not os.path.isdir(args.dir):
        print('Unable to find directory. Exiting')
        exit()


# check if log file currently exists, if it does delete it
if os.path.isfile(args.log):
    print('Removing previous log file.')
    os.remove(args.log)


# writes input to log file
def logWriter(message):
    logFile = open(args.log, 'a')
    logFile.write(message)
    logFile.writer(os.linesep)
    logFile.close()


# walk the dir to find the files that meet the size requirement
for root, dir, files in os.walk(args.dir):
    for file in files:
        try:
            size = os.path.getsize(os.path.join(root, file)) / 1048576  # get the size in MB
            if size >= args.size:
                logWriter('Size: ' + str(size) + '----' + os.path.join(root, file))
        except IOError as e:
            logWriter('ERROR: ' + os.path.join(root, file) + str(e))
