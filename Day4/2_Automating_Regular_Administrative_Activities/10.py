#!/usr/bin/env python 
#
# Read config file 
#
from __future__ import print_function 
from ConfigParser import SafeConfigParser 

parser = SafeConfigParser() 
parser.read('simple.ini')
print(parser.get('bug_tracker', 'url'))
