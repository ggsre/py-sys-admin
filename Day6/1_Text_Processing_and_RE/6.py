#!/usr/bin/env python
#
# Multiple Matches
#
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
  print 'Found "%s"' % match

for match in re.finditer(pattern, text):
  s = match.start()
  e = match.end()
  print 'Found "%s" at %d:%d' % (text[s:e], s, e)
