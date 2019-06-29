#!/usr/bin/env python 
# 
# Working with Excel Files - openpyxl - creating new file 
# 
from openpyxl import Workbook 

book_obj = Workbook() 
excel_sheet = book_obj.active
excel_sheet['A1'] = 'Name'
excel_sheet['A2'] = 'student'
excel_sheet['B1'] = 'age'
excel_sheet['B2'] = '20'

book_obj.save('test.xlsx') 
print 'Excel created successfully'
