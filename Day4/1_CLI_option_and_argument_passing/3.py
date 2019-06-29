#!/usr/bin/env python 
#
# Using argparse 
#
from __future__ import print_function 
import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%()s 1.0')
args = parser.parse_args()
print(args)
print(args.filename)
