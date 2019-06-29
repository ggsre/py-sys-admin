#!/usr/bin/env python 
#
# Raise exception when warning is raised 
#
from __future__ import print_function 
import warnings

warnings.simplefilter('error', UserWarning)
print('Before')

warnings.warn('This is a warning message')
print('After')
