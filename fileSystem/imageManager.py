# I needed a tool to help bring an unruly picture library together. It will read the meta data of all of the images
# found in the passed directory, create a folder structure of <YEAR\MONTH\DAY> and then move the image files into
# the correct folder based on the 'DATE TAKEN' meta data. If the meta data is absent, the image will be moved into a
# 'catchAll' directory

import os
import datetime
import time
import shutil
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description="Move image files (jpeg) info a folder structure <YEAR\\MONTH\\DAY>")
parser.add_argument('-s', '--src', help="The home directory of the image files.")
parser.add_argument('-d', '--dst', help="The location where you want to create the dir structure.")
parser.add_argument('-l', '--log', help="The name and logFile you want to create.", default="log.txt")

args = parser.parse_args()

print("\nRedArrowDriver\nImage Library Structure Creator 0.1\nMove image files (jpeg) info a folder structure "
      "<YEAR\\MONTH\\DAY>\n\n")

if args.src is None:
    args.src = input("Enter a home directory of the image files: ")
    if not os.path.isdir(args.src):
        print("Unreacheable dir: " + args.src + '. Existing application.')
        exit()

#check for previous log file, if exists delete
if os.path.isfile(args.src + '\\' + args.log):
    print("Removing previous log file.")
    os.remove(args.src + '\\' + args.log)



# createTime = (Image.open("F:\\temp\\pictures\\catch\\SnapChat-2130546790.jpg").getexif()[306])
createTime = time.ctime(os.path.getmtime("F:\\temp\\pictures\\catch\\SnapChat-2063693639.jpg"))
format = "%Y:%m:%d %H:%M:%S"
print(createTime)
# date = createTime.split(' ', 1)
# date2 = str(date[0]).split(':', 3)
# print("Type of date: " + str(type(date)))
# print("This is just the date: " + str(date[0]))
# print("This is the year: " + date2[0])
# print("This is the month: " + date2[1])
# print("This is the day: " + date2[2])
# print("Create Time = " + createTime)
# print(str.split(createTime, ':'))
# print(createTime.split(':', 2))
# justYear = createTime.split(':', 2)
# print("Just Year = " + justYear[0])
# yearString = str(justYear[0])
# print("String of the year: " + yearString)
# splitTime = createTime.split(':', 2)
# print(splitTime[2])
# justDay = str(splitTime[2])
# day = justDay[:2]
# print("Just the day: " + day)

def logWriter(message):
    logFile = open(args.src + '\\' + args.log, 'a')
    logFile.write(message + '\n')
    logFile.close()

# for root, dir, files in os.walk(args.dir):
#     for file in files:
#         try:
#             size = os.path.getsize(os.path.join(root, file)) / 1048576  # get the size in MB
#             if size >= args.size:
#                 logWriter('Size: ' + str(size) + '----' + os.path.join(root, file))
#         except IOError as e:
#             logWriter('ERROR: ' + os.path.join(root, file) + str(e))

def worker(filePath):
    for root, dir, files in os.walk(filePath):
        for file in files:
            try:
                createTimeArray = Image.open(os.path.join(root, file)).getexif()[36867]
                createTimeDateArray = createTimeArray.split(' ', 1)
                createDate = str(createTimeDateArray[0]).split(':', 3)
                createYear = str(createDate[0])
                createMonth = str(createDate[1])
                createDay = str(createDate[2])
                # file moving here
                if os.path.isdir(args.src + '\\' + createYear) is False:
                    os.mkdir(args.src + '\\' + createYear)
                if os.path.isdir(args.src + '\\' + createYear + '\\' + createMonth) is False:
                    os.mkdir(args.src + '\\' + createYear + '\\' + createMonth)
                if os.path.isdir(args.src + '\\' + createYear + '\\' + createMonth + '\\' + createDay) is False:
                    os.mkdir(args.src + '\\' + createYear + '\\' + createMonth + '\\' + createDay)
                shutil.move(os.path.join(root, file), args.src + '\\' + createYear + '\\' + createMonth + '\\' + createDay + '\\' + file)

            except IOError as e:
                logWriter('IO ERROR: ' + os.path.join(root, file) + str(e))
                print('ERROR: ' + os.path.join(root, file) + str(e))
                if os.path.isdir(args.src + '\\' + 'catch') is False:
                    os.mkdir(args.src + '\\' + 'catch')
                shutil.move(os.path.join(root, file), args.src + '\\' + 'catch' + '\\' + file)
            except EOFError as e:
                logWriter('EOF ERROR: ' + os.path.join(root, file) + str(e))
                print('ERROR: ' + os.path.join(root, file) + str(e))
                if os.path.isdir(args.src + '\\' + 'catch') is False:
                    os.mkdir(args.src + '\\' + 'catch')
                shutil.move(os.path.join(root, file), args.src + '\\' + 'catch' + '\\' + file)
            except:
                logWriter('ERROR: an unexpected error occured in file. This most likely means'
                          'that the date taken field is NULL: ' + os.path.join(root, file))
                if os.path.isdir(args.src + '\\' + 'catch') is False:
                    os.mkdir(args.src + '\\' + 'catch')
                shutil.move(os.path.join(root, file), args.src + '\\' + 'catch' + '\\' + file)


# worker(args.src)