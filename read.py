#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 读取文件

file = raw_input()
with open(file) as f:
    for line in f.readlines():
        print(line.strip())