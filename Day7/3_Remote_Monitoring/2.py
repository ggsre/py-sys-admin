#!?usr/bin/env python 
# 
# subprocess.Popen 
# 
import subprocess
import sys

HOST="127.0.0.1"
COMMAND= "ls"

ssh_obj = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
 shell=False,
 stdout=subprocess.PIPE,
 stderr=subprocess.PIPE)

result = ssh_obj.stdout.readlines()
if result == []:
 err = ssh_obj.stderr.readlines()
 print(sys.stderr, "ERROR: %s" % err)
else:
 print(result)
