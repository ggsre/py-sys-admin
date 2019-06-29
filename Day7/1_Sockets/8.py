#!/usr/bin/env python 
#
# urllib - access website 
# 
import urllib 

x = urllib.urlopen('https://www.imdb.com/')
print x.read() 

# urllib response headers
print '********************'
print 'Printing Headers now' 
print '********************'
print x.info() 
