#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 多线程

import time
import threading


def loop():
    print "thread %s is running..." % threading.currentThread().name
    n = 0
    while n < 5:
        n += 1
        print "thread %s >>> %s" % (threading.currentThread().name, n)
        time.sleep(1)
    print "thread %s is ended" % threading.currentThread().name


print "thrad %s is running..." % threading.currentThread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print "thread %s ended." % threading.currentThread().name
