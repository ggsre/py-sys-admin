#!/usr/bin/env python 
# 
# Example file for retrieving data from the internet
#
from __future__ import print_function 
import urllib2 

def main():
  # open a connection to a URL using urllib2
  webUrl = urllib2.urlopen("http://www.google.com")
  
  # get the result code and print it
  print ("result code: " + str(webUrl.getcode()))
  
  # read the data from the URL and print it
  data = webUrl.read()
  print (data)

if __name__ == "__main__":
  main()

