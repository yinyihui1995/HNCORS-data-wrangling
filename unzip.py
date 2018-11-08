import os
import zipfile

def unZip(rootDir):

    # 遍历目录下的文件/文件夹
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            unZip(path)
            continue

        if zipfile.is_zipfile(path):
            # 打印解压文件对应目录
            srcfile = zipfile.ZipFile(path)
            for filename in srcfile.namelist():
                try:
                    # 解压遍历到的文件至 saveDir (指定位置)
                    print("unzip " + path)
                    srcfile.extract(filename, saveDir)
                    # 计数
                    #number += 1
                    #print("completed " + str(number))
                except Exception:
                    print(path + "数据损坏！")
                else:
                    pass
            

# 待处理的文件目录
#file_path = '/Users/yinyihui/Desktop/2017data'
file_path = 'yourFilePath'

# 设置需要保存解压文件的目录
saveDir = file_path + "_files"
    
number = 0
unZip(file_path)
