#!/usr/bin/env python
#
# String formatting 
#
from __future__ import print_function 

print('Basic Formatting: Old Style') 
print('%s %s' % ('one', 'two'))
print('%d %d' % (1,2))

print('Basic Formatting: New Style')
print('{} {}'.format('one', 'two'))
print('{} {}'.format(1, 2))
print('Basic Formatting: re-arrange order')
print('{1} {0}'.format('one', 'two'))

print('Align Right: Old Style')
print('%10s' % ('test'))
print('Align Right: New Style')
print('{:>10}'.format('test'))

print('Align Left: Old Style')
print('%-10s' % ('test'))
print('Align Left: New Style')
print('{:10}'.format('test'))

print('Align and Padding: New Style')
print('{:_<10}'.format('test'))
print('Align Center: New Style')
print('{:^10}'.format('test'))
print('{:^6}'.format('zip'))

print('Truncating Long Strings: Old Style')
print('%.5s' % ('xylophone'))
print('Truncating Long Strings: New Style')
print('{:.5}'.format('xylophone'))

print('Padding Numbers: Old Style')
print('%4d' % (42,))
print('Padding Numbers: New Style')
print('{:4d}'.format(42))

print('Floating Point Precision: Old Style')
print('%06.2f' % (3.141592653589793,))
print('Floating Point Precision: New Style')
print('{:06.2f}'.format(3.141592653589793))

print('Pad Integers With Leading Zeros: Old Style')
print('%04d' % (42,))
print('Pad Integers With Leading Zeros: New Style')
print('{:04d}'.format(42))

data = {'first': 'John', 'last': 'Smith'}
print('Named Placeholders: Old Style')
print('%(first)s %(last)s' % data)
print('Named Placeholders: New Style')
print('{first} {last}'.format(**data))

print('Keyword Arguments: New Style')
print('{first} {last}'.format(first='John', last='Smith'))

