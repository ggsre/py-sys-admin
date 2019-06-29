#!/usr/bin/env python 
#
# Example file for formatting time and date output
#

from __future__ import print_function 
from datetime import datetime

def main():
  now = datetime.now()
  print("Year:")
  print(now.strftime("The current year is: %Y"))

  print("\nShort year:")
  print(now.strftime("%a, %d %B, %y"))

  print("\nLocale:")
  print(now.strftime("Locale date and time: %c"))
  print(now.strftime("Locale date: %x"))
  print(now.strftime("Locale time: %X"))

  print("\nTime:")
  print(now.strftime("Current Time: %I:%M:%S %p"))
  print(now.strftime("24-hour time: %H:%M"))



if __name__ == "__main__":
  main();

