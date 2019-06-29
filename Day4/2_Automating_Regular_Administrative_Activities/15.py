#!/usr/bin/env python 
#
# Making backups using rsync 
#
from __future__ import print_function 
import os 
import shutil 
import time 
from sh import rsync 

def check_dir(os_dir):
  if not os.path.exists(os_dir):
    print(os_dir, 'does not exist')
    exit(1)

def ask_for_confirmation():
  ans = raw_input('Do you want to continue? yes/no\n')
  global con_exit 
  if ans == 'yes':
    con_exit = 0
    return con_exit 
  elif ans == 'no':
    con_exit = 1
    return con_exit 
  else:
    print("Answer with yes or no")
    ask_for_confirmation() 

def delete_files(ending):
  for r, d, f in os.walk(backup_dir):
    for files in f:
      if files.endswith("." + ending):
        os.remove(os.path.join(r, files))

backup_dir = raw_input('Enter the directory to backup\n') 
check_dir(backup_dir) 
print(backup_dir, 'saved') 
time.sleep(3) 
backup_to_dir = raw_input('Where to backup?\n')
check_dir(backup_to_dir) 
print('Starting the backup now')
ask_for_confirmation() 
if con_exit == 1:
  print('Aborting the backup process')
  exit(1)

rsync("-auhv", "--delete", "--exclude=lost+found", "--exclude=/sys", "--exclude=/tmp", "--exclude=/proc", "--exclude=/mnt", "--exclude=/dev", "--exclude=/backup", backup_dir, backup_to_dir)

