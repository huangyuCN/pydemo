#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 多线程

import thrd
import time

def printTime(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s:%s" % (threadName,time.ctime(time.time()))

try:
    thrd.start_new_thread(printTime, ("Thread_1", 2))
    thrd.start_new_thread(printTime, ("Thread_2", 4))
except:
    print "Error:unable to start thread"

while 1:
    pass

