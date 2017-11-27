# -*- coding: UTF-8 -*-
import subprocess, shlex

command_line = raw_input()
args = shlex.split(command_line)
child1 = subprocess.Popen(args, stdout=subprocess.PIPE)
print child1.stdout.read()
# 或者 child1.communicate() #communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成

cat = "cat ./thrd.py"
cat_args = shlex.split(cat)
child2 = subprocess.Popen(cat_args, stdout=subprocess.PIPE)
child3 = subprocess.Popen(["grep", "count += 1"], stdin=child2.stdout, stdout=subprocess.PIPE)
print child3.communicate()

grep = "cat ./thrd.py | grep 'count += 1'"
subprocess.Popen(grep, shell=True)
