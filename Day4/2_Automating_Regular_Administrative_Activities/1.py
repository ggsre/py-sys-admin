#!/usr/bin/env python 
#
# redirection.py 
#
from __future__ import print_function 
import sys 

class Redirection(object):
  def __init__(self, in_obj, out_obj):
    self.input = in_obj 
    self.output = out_obj
  def read_line(self):
    res = self.input.readline() 
    self.output(res) 
    return res 

if __name__ == '__main__':
  if not sys.stdin.isatty():
    sys.stdin = Redirection(in_obj=sys.stdin, out_obj=sys.stdout)

  a = raw_input('Enter a string: ')
  b = raw_input('Enter another string: ')
  print('Entered strings are:', repr(a), 'and', repr(b))
