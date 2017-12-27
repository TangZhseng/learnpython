#学习之用
import sys
import re
import time
def log(flag):
  def show(f):
    def inner(*x,**y):
        start=time.time()
        f(*x,**y)
        end=time.time()
        print('spend %s' % (end-start))
        print(flag)
    return inner
  return show
@log('ture')
def f(x,y):
    print(x+y)
f(1,2)