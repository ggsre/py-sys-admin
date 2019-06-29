#!?usr/bin/env python 
# 
# ftplib - downloading files from a ftp server 
# 
import os
from ftplib import FTP

ftp = FTP('your-ftp-domain-or-ip')
with ftp:
    ftp.login('your-username','your-password')
    ftp.cwd('/home/student/work/')
    files = ftp.nlst()
    print(files)
    # Print the files
    for file in files:
        if os.path.isfile(file):
            print("Downloading..." + file)
            ftp.retrbinary("RETR " + file ,open("/home/student/testing/" + file, 'wb').write)

ftp.close()
