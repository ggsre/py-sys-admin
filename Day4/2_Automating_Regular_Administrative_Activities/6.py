#!/usr/bin/env python 
#
# Capturing output using subprocess 
#
from __future__ import print_function 
import subprocess 

result = subprocess.check_output(['ls','-l'])

print(result)
