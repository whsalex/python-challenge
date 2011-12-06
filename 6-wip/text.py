#!/usr/bin/python2.6
import os
import re

filepath=os.path.join(os.path.abspath("."),"channelfile")

# hint1: start from 90052
startfile="90052"
pattern=re.compile("Next nothing is ([0-9]*)$")
temp=startfile

while True:
    ofile=filepath+os.path.sep+temp+".txt"
    fd=file(ofile,"r")
    for line in fd:
        print line
        result=re.search(pattern,line)
        if result is not None:
           for no in result.groups():
               #print no
               temp=no
           #break for if find a match string
           break
        else:
           print line
    else:
        break
