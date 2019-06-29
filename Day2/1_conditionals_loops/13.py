#!/usr/bin/env python 
from __future__ import print_function

numbers = [10, 25, 54, 86, 89, 11, 33, 22]
new_numbers = list(filter(lambda x: (x%2 == 0) , numbers))
print(new_numbers)
