#!/usr/bin/env python 
#
# Input by input file 
#
from __future__ import print_function 

input_file = open('sample.txt', 'r')
output_file = open('sample_out.txt', 'w')

data = input_file.read() 
output_file.write(data) 
