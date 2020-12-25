#replace
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah','yep'))
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))
print(re.sub(r'(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)', r'\g<year>-\g<month>-\g<day>', text))

