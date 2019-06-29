#!/usr/bin/env python 
# 
# Socket - client.py 
# 
import socket 

host_name = socket.gethostname() 
port = 5555 

c_socket = socket.socket() 
c_socket.connect((host_name, port))
msg = raw_input(" -> ")

while msg.lower().strip() != 'bye':
  c_socket.send(msg.encode())
  recv_data = c_socket.recv(1024).decode() 
  print 'Received from server:', recv_data
  msg = raw_input(" -> ") 

c_socket.close() 
