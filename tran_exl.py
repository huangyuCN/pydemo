# -*- coding: UTF-8 -*-
import os
import sys

pyDir = "/Works/Development/python/tranExcel/tran.py"
dstFolder = "/Users/HuangYu/Downloads/tran_exl/conf"
md5Folder = "/Users/HuangYu/Downloads/tran_exl/md5"
srcFolder = "/Works/Document/svn/hookheroes/dr3/cfg_dev"
# srcFolder = "/Users/HuangYu/Downloads/exl"
clean = ""
if len(sys.argv) > 1 and sys.argv[1] == "-c":
    clean = "-c"
    os.system("rm -rf " + dstFolder + "/*")
    os.system("rm -rf " + md5Folder + "/*")
md5File = md5Folder + "/excel_md5.txt"
# python tran.py "srcFolder" "dstFolder" "md5File" "-c"
os.system("python " + pyDir + " " + srcFolder + " " + dstFolder + " " + md5File + " " + clean)
