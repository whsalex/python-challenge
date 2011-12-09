#!/usr/bin/python2.6
from PIL import Image
import os
import re

#PNG file
png=os.path.join(os.path.abspath("."),"oxygen.png")

im=Image.open(png)

string=""
temp=im.getpixel((0,43))
string+=chr(temp[0])

for i in range(0,608):
    for j in range(43,52):
        new=im.getpixel((i,j))
        if temp == new :
            pass
        else:
            string+=chr(new[0])
            temp=new
print string+"\n"+"-"*60

key=re.search("\[(.*)\]$",string)
if key is not None:
    keystring=key.groups(1)[0]
else:
    print "no list"
print keystring

new_string=""
numlist=re.split(", ",keystring)
for num in numlist:
    t_num=int(num)
    if t_num<=122 and t_num>=97:
        pass
    else:
        #try t_num%26+97
        t_num=t_num+100
    new_string+=chr(t_num)
print new_string
#for num in numlist:
#    print chr(int(num))
