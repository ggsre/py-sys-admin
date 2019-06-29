#!/usr/binenv python
#
# Read apache log file 
# 
def read_apache_log(logfile):
  with open(logfile) as f:
    log_obj = f.read()
    print(log_obj)

if __name__ == '__main__':
  read_apache_log("access1.log")
