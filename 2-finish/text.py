#!/usr/bin/python2.6

inputfile='/home/wanghs/practise/python/python-challenge/2-wip/file'

fd=file(inputfile,"r")
lines=[line.strip() for line in fd.readlines()]
fd.close()

words={}

for i in lines:
    for j in i:
        if words.has_key(j):
            words[j]+=1
        else:
            words[j]=1

for wd in words:
    print wd,": ",words[wd] 
