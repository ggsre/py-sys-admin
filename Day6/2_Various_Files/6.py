#!/usr/bin/env python 
# 
# Working with Excel Files - Pandas 
# 
import pandas as pd 

excel_file = r'sample.xlsx'
df = pd.read_excel(excel_file) 
print df.head() 
