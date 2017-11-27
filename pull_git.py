#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess,os

folder = raw_input()
dir = "/home/dhcd/dhboss/source/" + folder
os.chdir(dir)
pwd = subprocess.call("pwd", shell=True)
print pwd
checkout = subprocess.call("git checkout develop", shell=True)
print "git checkout develop"
print checkout
print "git pull"
pull = subprocess.call("git pull", shell=True)
print pull
