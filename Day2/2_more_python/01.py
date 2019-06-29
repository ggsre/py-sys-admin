#!/usr/bin/env python 
from __future__ import print_function

try:
  num1 = 7
  num2 = 0
  print(num1 / num2)
  print("Done calculation")
except ZeroDivisionError:
  print("An error occurred")
  print("due to zero division")
