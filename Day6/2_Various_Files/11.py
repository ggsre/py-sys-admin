#!/usr/bin/env python 
# 
# Working with CSV files - writing 
# 
import csv 

write_csv = [['Name', 'Sport'], ['Maradona', 'Football'], ['Sachin', 'Cricket'], ['Lionel Messi', 'Football']]

with open('csv_write.csv', 'w') as csvfile: 
  writer = csv.writer(csvfile) 
  writer.writerows(write_csv) 
  print write_csv
