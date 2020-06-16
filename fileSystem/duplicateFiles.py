# duplicateFiles will read all of the files in directory and its subdirectories looking for files that have the same
# md5 hash. This will help find duplicate files and possible space/bandwidth/time savings.
# Writes to a log file in the format of md5 hash,file location

import hashlib
import os
import argparse

parser = argparse.ArgumentParser(description='Find files with a matching md5 hash.')
parser.add_argument('-d', '--dir', help='The directory to scan')
parser.add_argument('-l', '--log', help='The location of the log file.', default='duplicateFiles.txt')
args = parser.parse_args()

print('RedArrowDriver\n\nDuplicate Files Version 0.1\nHelps find duplicate files.')

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

# declare hash value list
fileList = []
hashList = []
duplicateList = []

# writes input to log file
def logWriter(message):
    logFile = open(args.log, 'a')
    logFile.write(message + os.linesep)
    logFile.close()

def hashFunc(file):
    md5Hash = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5Hash.update(chunk)
    hash = md5Hash.hexdigest()
    return hash

def duplicateFinder(list, hashValue):
    count = 0
    for i in list:
        if i == hashValue:
            count = count + 1
        if count > 1:
            duplicateList.append(hashValue)

def dirHash():
    for root, dir, files in os.walk(args.dir):
        for file in files:
            fileList.append(hashFunc(os.path.join(root, file)) + ',' + os.path.join(root, file))
            hashList.append(hashFunc(os.path.join(root, file)))
            duplicateFinder(hashList, hashFunc(os.path.join(root, file)))
    for file in fileList:
        if file.split(',')[0] in duplicateList:
            logWriter('Duplicate File: ' + file)

dirHash()