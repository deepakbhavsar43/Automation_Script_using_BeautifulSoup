import os

basepath = '1Rivet'
dir = os.walk(basepath)
fileList = []


def joinPath(path, file):
    path = path + file
    return path


for path, subdirs, files in dir:
    # print(f"path : {path}\nsubdir : {subdirs}\nfiles : {files}\n")
    for file in files:
        temp = joinPath(path + '\\', file)
        fileList.append(temp)

for i in fileList:
    try:
        with open(i) as f:
            print(i)
    except IOError:
        print("File not accessible")
