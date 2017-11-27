#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 工作中用来监控日志的脚本

import subprocess, os, sys, shlex

print "please make sure the py running in the ~ folder"
pid = None
try:
    args = sys.argv
    if len(args) < 2:
        print "need 2 args, svr name and log type"
    else:
        svr = args[1]
        logDir = "./release/" + svr + "/log/console.log"
        crashDir = "./release/" + svr + "/log"
        shell = ""
        if args[2] == "log":
            if not os.path.exists(logDir):
                print "did not find log file"
            else:
                shell = "tail -f " + logDir
        elif args[2] == "crash":
            dir = crashDir + "/crash.log"
            if not os.path.exists(dir):
                dir = crashDir + "/crash.log.0"
            if not os.path.exists(dir):
                print "did not find crash log file"
            else:
                shell = "tail -f " + dir
        else:
            print "the 2nd arg is incorrect"

        if shell == "":
            print "args error"
        else:
            list = shlex.split(shell)
            print "args: ", list
            pid = subprocess.Popen(list)
            pid.communicate()
except:
    if pid == None:
        pass
    else:
        pid.terminate()
        print "terminate"
