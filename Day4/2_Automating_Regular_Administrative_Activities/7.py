#!/usr/bin/env python 
#
# Prompts for password and validates
#
from __future__ import print_function 
import getpass 

try:
  p = getpass.getpass() 
except Exception as error:
  print("ERROR", error) 
else:
  print("Password entered is:", p)
