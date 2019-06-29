#!/usr/bin/env python 
#
# Input by pipe 
#
from __future__ import print_function 
import sys

for n in sys.stdin:
  print( int(n.strip()) // 2)
