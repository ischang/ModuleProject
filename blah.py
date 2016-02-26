import re

foo = """ 
set name "foobar" 
set version "2.9999"
set description "a quick brown fox jumped over
a lazy dog"
set tags "blah, blah, blah"
"""

#pattern = re.compile("set\s(\w)\s\"([^\"])\"")
pattern = re.compile("set\s(\w+)\s\"(.+?)\"", re.DOTALL)

print re.findall(pattern, foo)

