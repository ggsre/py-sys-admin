#!/usr/bin/env python 
# 
# Creating a table in sqlite 
# 
import sqlite3

con_obj = sqlite3.connect("test.db")
with con_obj:
  cur_obj = con_obj.cursor()
  cur_obj.execute("""CREATE TABLE books(title text, author text)""")

print ("Table created")
