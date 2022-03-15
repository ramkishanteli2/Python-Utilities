import os
import sys
from PIL import Image
# os is inbuilt module in python
# It is used to perform many tasks
currDir = sys.argv[1]
newDir = sys.argv[2]

allFiles = os.listdir(os.getcwd())
newDirPath = os.getcwd()+"/" + newDir
currPath = os.getcwd()+"/"+currDir
if currDir not in allFiles:
    raise Exception(currDir + " does not exists")

if newDir not in allFiles:
    os.mkdir(newDirPath)

for file_ in os.listdir(currPath):
    if file_.endswith('.jpg'):
        img = Image.open(currPath+"/"+file_)
        file_ = file_.replace('.jpg', '.png')
        img.save(newDirPath+"/"+file_, 'png')
