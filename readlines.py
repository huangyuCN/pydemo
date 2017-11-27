#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 多行读取

import time

file = raw_input()
p = 0
haveline = True
with open(file, 'r+') as f:
    f.seek(p, 0)
    while haveline:
        lines = f.readlines()
        print "lines ", lines
        if lines:
            print lines
            p = f.tell()
            f.seek(p, 0)
        else:
            haveline = False
        time.sleep(1)
