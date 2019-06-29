#!/usr/bin/env python
#
# Working with Excel Files - xlrd - extracting names of columns
#
import xlrd 

excel_file = r'sample.xlsx'
book_obj = xlrd.open_workbook(excel_file) 
excel_sheet = book_obj.sheet_by_index(0) 
excel_sheet.cell_value(0, 0)
for i in range(excel_sheet.ncols):
  print excel_sheet.cell_value(0, i) 
