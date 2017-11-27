#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在其实位置匹配
