#!/usr/bin/env python 
# 
# Working with CSV files 
# 
import csv 

csv_file = open(r'test.csv', 'r')
with csv_file:
  read_csv = csv.reader(csv_file) 
  for row in read_csv:
    print row 
