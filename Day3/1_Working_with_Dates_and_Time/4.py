#!/usr/bin/env python 
#
# Example file for working with timedelta objects
#

from __future__ import print_function 
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta 

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print("Today is: " + str(now))

print("one year from now it will be: " + str(now + timedelta(days=365)))

print("In 2 days and 3 weeks it will be: " + str(now + timedelta(days=2, weeks=3)))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was: " + str(s))

today = date.today() 
afd = date(today.year, 4, 1) 
if afd < today:
  print("April Fool's Day already went by %d days ago" % ((today-afd).days))
  afd = afd.replace(year = today.year+1) 

time_to_afd = afd - today 
print("It's just", time_to_afd.days, "days until the next April Fool's Day")

