#!/usr/bin/env python 
#
#
#
from __future__ import print_function 
import getpass 

passwd = getpass.getpass(prompt='Enter your password: ')
if len(passwd) < 8:
  print("ERROR: password should be atleast contain atleast 8 characters")
else:
  print("OK: password length passed")
