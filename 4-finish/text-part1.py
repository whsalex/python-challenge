#!/usr/bin/env python

#Initial url is "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

from urllib import urlopen
import re

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
temp_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

pattern=re.compile(r".* the next nothing is ([0-9]*)$")

while True:
    urlfd=urlopen(temp_url)
    
    for line in urlfd.readlines():
        #Find out the line.
        print line
        reg=re.search(pattern,line)
        if reg is not None:
            for no in reg.groups():
               temp_url=url+no 
            break
        else:
           print "Done!"+"-"*20
        #Action.if not break,break while
    else:
        break 
