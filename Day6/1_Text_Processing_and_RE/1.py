#!/usr/bin/env python

import textwrap

sample_text = '''
        The textwrap module can be used to format text for output in situations
        where pretty-printing is desired.  It offers programmatic functionality similar
        to the paragraph wrapping or filling features found in many text editors.
        '''

#s = '''
# Filling Paragraphs
print 'No dedent:\n'
print textwrap.fill(sample_text)
#'''

# Removing Existing Indentation
dedented_text = textwrap.dedent(sample_text).strip()
print
print 'Dedented:\n'
print dedented_text

# Combining Dedent and Fill
dedented_text = textwrap.dedent(sample_text).strip()
for width in [ 20, 60, 80 ]:
  print
  print '%d Columns:\n' % width
  print textwrap.fill(dedented_text, width=width)

# Hanging Indents
dedented_text = textwrap.dedent(sample_text).strip()
print textwrap.fill(dedented_text, initial_indent='', subsequent_indent='    ')
