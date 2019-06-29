#!/usr/bin/env python 
#
# Using argparse 
#
from __future__ import print_function 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
args = parser.parse_args()
