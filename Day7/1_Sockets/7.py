#!?usr/bin/env python 
# 
# ftplib - Sending commands to the server
from ftplib import FTP

ftp = FTP('your-ftp-domain-or-ip')
ftp.login('your-username','your-password')

ftp.cwd('/home/student/')
s_cmd_stat = ftp.sendcmd('STAT')
print(s_cmd_stat)
print()

s_cmd_pwd = ftp.sendcmd('PWD')
print(s_cmd_pwd)
print()

ftp.close()
