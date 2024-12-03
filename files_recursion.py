# 递归遍历文件
import os
allfiles = []
def getFiles(path,level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filePath = os.path.join(path,file)
        if os.path.isdir(filePath):
            getFiles(filePath,level+1)
        allfiles.append("\t"*level+filePath[filePath.rfind(os.sep)+1:])

getFiles(r'G:\2024-08-07  新工作文档',0)

for f in reversed(allfiles):
    print(f)
