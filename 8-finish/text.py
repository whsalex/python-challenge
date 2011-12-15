#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/def/integrity.html

import urllib
import re
from bz2 import decompress

page=urllib.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html')
filelines=[line.strip() for line in page.readlines()]
page.close()

for li in filelines:
    unpattern=re.search("^un: '(.*)'",li)
    pwpattern=re.search("^pw: '(.*)'",li)
    if unpattern is not None:
        uname=unpattern.groups()[0]
        #print "User name string: %s" % uname
    if pwpattern is not None:
        pword=pwpattern.groups()[0]
        #print "Pass word string: %s" % pword

#Why always wrong...
#print "User name: %s" % decompress(uname)
#print "Pass word: %s" % decompress(pword)
print uname
print pword
