#!/usr/bin/env python
#
# Working with Excel Files - xlrd 
#
import xlrd 

excel_file = r'sample.xlsx'
book_obj = xlrd.open_workbook(excel_file) 
excel_sheet = book_obj.sheet_by_index(0) 
result = excel_sheet.cell_value(0, 1)
print result 
