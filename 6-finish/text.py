#!/usr/bin/python2.6
import os
import re
import zipfile

filepath=os.path.join(os.path.abspath("."),"channelfile")
zipf=os.path.join(os.path.abspath("."),"channel.zip")

# hint1: start from 90052
startfile="90052"
pattern=re.compile("Next nothing is ([0-9]*)$")
temp=startfile
string=""

#get the zip object
zip=zipfile.ZipFile(zipf)
#extact the files
zip.extractall('/home/wanghs/practise/python/python-challenge/6-wip/channelfile')

while True:
    #Get the comment from all file
    string+=zip.getinfo(temp+'.txt').comment

    ofile=filepath+os.path.sep+temp+".txt"
    fd=file(ofile,"r")
    for line in fd:
        result=re.search(pattern,line)
        if result is not None:
           for no in result.groups():
               # print no
               # Find the next file to read
               temp=no
           #break for if find a match string
           break
        else:
           pass #print line
    else:
        break

print "-"*25+" Done ! "+"-"*25+"\n"+string
