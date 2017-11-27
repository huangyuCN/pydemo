#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 用来导出代码的脚本

import os
import sys

pyDir = ""
dstFolder = ""
md5Folder = ""
srcFolder = ""
# srcFolder = "/Users/HuangYu/Downloads/exl"
clean = ""
if len(sys.argv) > 1 and sys.argv[1] == "-c":
    clean = "-c"
    os.system("rm -rf " + dstFolder + "/*")
    os.system("rm -rf " + md5Folder + "/*")
md5File = md5Folder + "/excel_md5.txt"
# python tran.py "srcFolder" "dstFolder" "md5File" "-c"
os.system("python " + pyDir + " " + srcFolder + " " + dstFolder + " " + md5File + " " + clean)
