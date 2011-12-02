#!/usr/bin/python2.6

import re

fd=file("/home/wanghs/practise/python/python-challenge/3-wip/file","r")
lines=[line.strip() for line in fd.readlines()]
fd.close

word=""

for mline in lines:
    match=re.search("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]",mline)
    if match is not None:
        for i in match.groups():
            word+=i

print word
