#!/usr/bin/env python 
from __future__ import print_function

try:
  word = "spam"
  print(word / 0)
except:
  print("An error occurred")
