#你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
result = re.split(r'[;,\s]\s*',line)
print(result)
result = re.split(r'(;|,|\s)\s*',line)
print(result)
result = re.split(r'(?:;|,|\s)\s*',line)
print(result)
