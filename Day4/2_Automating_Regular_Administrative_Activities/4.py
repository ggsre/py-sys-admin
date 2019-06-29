#!/usr/bin/env python 
#
# Handling passwords 
#
from __future__ import print_function 
import sys 
import paramiko 

ip_address = "127.0.0.1"
username = "student"
password = "redhat"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip_address,\
                                    username=username, password=password)
print ("Successful connection", ip_address)
ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('cd /tmp; mkdir work\n')
remote_connection = ssh_client.exec_command('cd /tmp/work; mkdir test_folder\n')
#print( remote_connection.read() )
ssh_client.close
