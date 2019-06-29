#!/usr/bin/env python 
# 
# Working with Excel Files - openpyxl - reading multiple cells 
# 
import openpyxl 

book_obj = openpyxl.load_workbook(r'sample.xlsx')
excel_sheet = book_obj.active
cells = excel_sheet['A1': 'C6']
for c1, c2, c3 in cells:
  print "{0:6} {1:6} {2:6}".format(c1.value, c2.value, c3.value)
