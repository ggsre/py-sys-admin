#!/usr/bin/env python 
from __future__ import print_function

numbers = [10, 20, 30, 40]

numbers_iter = iter(numbers)

print(next(numbers_iter))
print(next(numbers_iter))
print(numbers_iter.next())
print(numbers_iter.next())
print(next(numbers_iter))
