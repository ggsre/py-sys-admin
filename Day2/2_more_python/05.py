#!/usr/bin/env python 
from __future__ import print_function

try:
  print(1)
  print(10 / 0)
except ZeroDivisionError:
  print(unknown_var)
finally:
  print("This is executed last")
