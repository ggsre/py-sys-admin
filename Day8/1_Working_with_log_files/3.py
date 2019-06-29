#!/usr/bin/env python 
# 
# Parsing other log files 
# 
f=open('/var/log/dmesg','r')

lines = f.readlines()
for line in lines:
  kern_log = line.split()
  print(kern_log)

f.close()
