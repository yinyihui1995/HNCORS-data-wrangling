#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
time1 = time.time()

# def mergeFiles (meragefiledir):
#     filenames = os.listdir(meragefiledir)
#     file = open('test.17d','w')

#     for filename in filenames:
#         filepath = meragefiledir + '\\' + filename

#         for line in open(filepath):
#             file.writelines(line)
#         file.write('\n')

#     file.close()


#      print('finished')

meragefiledir = os.getcwd() + '\\MerageFiles'

filenames = os.listdir(meragefiledir)

file = open('test.17d','w')

for filename in filenames:
    filepath = meragefiledir + '\\' + filename

    for line in open(filepath):
        file.writelines(line)
    file.write('\n')

file.close()


# def openFiles (filepath):
#     filename = 'CDAX001aB.17D'
#     with open(filename) as file_object:
#         for line in file_object:
#             print(line)

if __name__ == '__main__':
    # filepath="D:/course/"
    # outfile="result.txt"
    # MergeTxt(filepath,outfile)
    # time2 = time.time()
    # print (u'总共耗时：' + str(time2 - time1) + 's')