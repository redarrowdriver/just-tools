# I needed a tool to help bring an unruly picture library together. It will read the meta data of all of the images
# found in the passed directory, create a folder structure of <YEAR\MONTH\DAY> and then move the image files into
# the correct folder based on the 'DATE TAKEN' meta data. If the meta data is absent, the image will be moved into a
# 'catchAll' directory

from PIL import Image
createTime = (Image.open("F:\\media\\Pictures\\2008\\06\\15\\PICT0290.JPG").getexif()[36867])
print(createTime)
print(type(createTime))
print(str.split(createTime, ':'))
print(createTime.split(':', 2))
splitTime = createTime.split(':', 2)
print(splitTime[2])
justDay = str(splitTime[2])
day = justDay[:2]