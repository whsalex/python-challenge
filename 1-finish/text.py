#!/usr/bin/env python

string=raw_input('Please input: ')
for char in range(len(string)):
    if ( ord(string[char]) <= 122 ) and ( ord(string[char]) >= 97):
        int = (ord(string[char])+2-97)%26+97
    else:
        int = ord(string[char])
    print chr(int),

#Note:
#String not support modify function.But could using +=
#So a better way: s=""; s+="chr((ord(string[char])+2-97)%26+97)"

#Or using  string.translate("xxx",string.maketrans("abc...xyz","cde...zab"))
