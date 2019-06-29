#!/usr/bin/env python 
#
# Executing external commands
#
from __future__ import print_function 
import subprocess 

subprocess.call(['touch', 'subprocess_test.txt'])
subprocess.call(["ls"])
print("Sample File created")
subprocess.call(['rm', 'subprocess_test.txt'])
print("Sample File Removed")
subprocess.call(["ls"])
