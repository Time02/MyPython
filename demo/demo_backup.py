#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

print(os.getcwd())

source = ['D:\\hechen\\php7\\myPython\\demo'] # 需要备份的文件和目录
# source = ['/home/test/'] # limux

target_dir = 'D:\\hechen\\php7\\myPython\\backup\\' # 备份目录的位置
# target_dir = '/backup/' # 备份目录的位置

today = target_dir + time.strftime('%Y%m%d') # 文件夹名

now = time.strftime('%H%M%S') # 文件名

comment = input('请输入备注：--&gt')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +  comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.makedirs(today)
    print('Successfully creat  directory', today)

zip_command = "zip -qr '%s' %s" % (target, ''.join(source)) # 使用 linux 的zip 命令
tar = 'tar -cvzf %s %s -X /home/swaroop/excludes.txt' % (target, ' '.join(source)) # tar 命令更快更小

#-c表示创建一个归档。
#-v表示交互，即命令更具交互性。
#-z表示使用gzip滤波器。
#-f表示强迫创建归档，即如果已经有一个同名文件，它会被替换。
#-X表示含在指定文件名列表中的文件会被排除在备份之外。例如，你可以在文件中指定*~，从而不让备份包括所有以~结尾的文件。
if os.system(zip_command) == 0: #在shell中运行命令——如果命令成功运行，它返回0，否则它返回错误号
    print('Successful backup to', target)
else:
    print('back up faild')

# 分别使用 Python 的标准库， zipfile和tarfile  os 会出现一些错误
