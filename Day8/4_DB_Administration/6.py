#!/usr/bin/env python 
# 
# Connecting to sqlite db 
# 
import sqlite3

con_obj = sqlite3.connect('test.db')
print ("Database connected successfully !!")
