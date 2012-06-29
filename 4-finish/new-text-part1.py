#!/usr/bin/env python

#Initial url is "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

from urllib import urlopen
import re

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
temp_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

pattern=re.compile(r".* the next nothing is ([0-9]*)$")

# Rewrite for a better understand coding.
found_flag=False
next_flag=True

while found_flag == False:
    urlfd=urlopen( temp_url )

    if next_flag==True:

        next_flag=False
        for line in urlfd.readlines():
            print line
        
            reg=re.search(pattern,line)

            if reg is not None:
                for number in reg.groups():
                    temp_url=url+number
                    next_flag=True
    else:  # next_flag==False
        # Didn't find any match str. Finished the search.
        break

print "Done!"+"-"*20
