#!/usr/bin/env python

import re
patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
  print 'Looking for "%s" in "%s" ->' % (pattern, text),

  if re.search(pattern,  text):
    print 'found a match!'
  else:
    print 'no match'
bash-4.1$ python 3.py
Looking for "this" in "Does this text match the pattern?" -> found a match!
Looking for "that" in "Does this text match the pattern?" -> no match
