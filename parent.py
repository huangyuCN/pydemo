#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:
    parentAttr = 100

    def __init__(self):
        print "Parent init"

    def parentMethod(self):
        print "Parent method"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "ParentAttr:", Parent.parentAttr

    def myMethod(self):
        print "Parent mythod"


class Child(Parent):
    def __init__(self):
        print "child init"

    def childMethod(self):
        print "child method"

    # 调用父类的方法
    def myMethod(self):
        Parent.myMethod(self)
        print "child mymethod"


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMethod()
