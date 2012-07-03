#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/bull.html

import sys
import types

def usage():
    print '''
Usage: ./text.py STOPINT
STOPINT (a int) is the lens of list,since it is infinte.
    '''

def checkArgv():
    argc=len(sys.argv)
    if argc != 2:
        usage()
	return 1

    try:
        int(sys.argv[1])
    except ValueError, reason:
        print "STOPINT should be a integer," ,reason
        usage()
        return 1
    #if type(int(sys.argv[1])) is not types.IntType: 
    #	usage()
    #	return 1

def nextStr(p_str):
    '''
Generate next number.List cell division.
1 -> 11, 2 - >12, 11 -> 21.
    '''

    string=""
    flag=False

    length=len(p_str)
 
    for i in range(length):
	if flag:
	    flag=False
            continue

        if p_str[i] == '2':
            string+='12'
	#Not the last one and value is '11'.
        elif (i+1) < length and p_str[i+1] == '1':
            string+='21'
	    #Jump to the next two char
	    flag=True
	else:
	    string+='11'

    return string

def main():
    
    if checkArgv():
        return -1

    rList=['1']
    listNum=len(rList)

    while listNum < int(sys.argv[1]):

       new_str=nextStr(rList[-1])

       rList.append(new_str)
       listNum=len(rList)

    #Should comment next line when sys.argv[1] beyond 20.So many.
    #print rList
    #print "Result 'a' list is: ",rList
    print "The %s(th) 's length is: %d." % ( sys.argv[1],len(bin(int(rList[-1]))) )

if __name__=='__main__':
    main()
