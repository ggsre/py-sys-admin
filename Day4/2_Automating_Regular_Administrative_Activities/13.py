#!/usr/bin/env python 
#
# Logging warning codes 
#
from __future__ import print_function 
import logging
import warnings

LOG_FILENAME = 'log.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO,)
warnings.warn('This warning is not sent to the logs')
logging.captureWarnings(True)
warnings.warn('This warning is sent to the logs')
