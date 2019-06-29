#!/usr/bin/env python 
from __future__ import print_function

try:
  variable = 10
  print(variable + "hello")
  print(variable / 0)
except ZeroDivisionError:
  print("Divided by zero")
except (ValueError, TypeError):
  print("Error occurred")
