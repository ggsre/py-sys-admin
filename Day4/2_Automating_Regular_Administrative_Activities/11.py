#!/usr/bin/env python 
#
# Read more than one file using configparser
#
from __future__ import print_function 
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()

candidates = ['does_not_exist.ini', 'also-does-not-exist.ini',
              'simple.ini', 'multisection.ini',
              ]

found = parser.read(candidates)

missing = set(candidates) - set(found)

print('Found config files:', sorted(found))
print('Missing files     :', sorted(missing))
