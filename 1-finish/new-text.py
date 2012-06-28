#!/usr/bin/env python

string="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

#string=raw_input('Please input: ')
result=""
for char in range(len(string)):
    if ( ord(string[char]) <= 122 ) and ( ord(string[char]) >= 97):
        result+=chr( (ord(string[char])+2-97)%26+97 )
    else:
        result+=chr( ord(string[char]) )

print result

#Note:
#String not support modify function.But could using +=
#So a better way: s=""; s+="chr((ord(string[char])+2-97)%26+97)"

#Or using  string.translate("xxx",string.maketrans("abc...xyz","cde...zab"))
