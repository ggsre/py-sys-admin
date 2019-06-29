#!/usr/bin/env python 
# 
# Working with Excel Files - Pandas 
# 
import pandas as pd 

excel_file = r'sample.xlsx'
cols = [1, 2, 3]
df = pd.read_excel(excel_file, usecols=cols) 
print df.head() 
