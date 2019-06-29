#!/usr/bin/env python
#
# Example file for working with date information
#
from __future__ import print_function 
from datetime import date 
from datetime import time
from datetime import datetime 


def main():
  today = date.today() 
  print("Today's date is", today) 
  print("Date Components:", today.day, today.month, today.year) 
  print("Today's weekday # is", today.weekday())
  days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
  print("which is a:", days[today.weekday()])

  print("\nWorking with date and tie now.")
  today = datetime.now()
  print("The current date and time is", today)

  
  print("\nTime portion")
  t = datetime.time(datetime.now())
  print("Now the time is", t) 

if __name__ == "__main__":
  main();
  

