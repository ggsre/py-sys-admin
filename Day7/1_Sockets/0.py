#!/usr/bin/env python 
# 
# Info about Sockets 
# 
print 'A socket is one endpoint of a communication channel used by programs to pass data back and forth locally or across the Internet'
print 'Sockets have two primary properties controlling the way they send data' 
print '	-> the address family controls the OSI network layer protocol'
print ' ->  the socket type controls the transport layer protocol'
print 
print 'Python supports three address families'
print ' -> AF_INET, is used for IPv4 Internet addressing'
print ' -> AF_INET, is used for IPv4 Internet addressing'
print ' -> AF_UNIX is the address family for Unix Domain Sockets (UDS)'
print 
print 'Syntax to create a socket is: socket.socket(address_family, socket type)' 
print 'The socket type is usually either SOCK_DGRAM for user datagram protocol (UDP) or SOCK_STREAM for transmission control protocol (TCP)'
print 
print 'To lookup hostname: socket.gethostname()'
print 'To lookup IP: socket.gethostbyaddr(IPADDRESS)'
