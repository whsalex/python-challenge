#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/bull.html

import sys
import types

rList=['1']

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

def nextStr(p_str):
    '''
Generate next number...Just pronounce it.
    '''

    string=""
    temp_str=p_str[0]
    temp_int = 0
    length=len(p_str)

    # Actually,no need to use range length.
    # Could use 'for i in p_str' directly
    for i in range(length):
        if temp_str==p_str[i]:
            temp_int+=1

        else:
	    #Add the last info when not match.
            string+=str(temp_int)+temp_str
            temp_str=p_str[i]
            temp_int=1

    #Flash the last date to string
    string+=str(temp_int)+temp_str
    
    return string

def main():
    
    if checkArgv():
        return -1

    listNum=len(rList)

    while listNum < int(sys.argv[1]):

       new_str=nextStr(rList[-1])

       rList.append(new_str)
       listNum=len(rList)

    #Should comment next line when sys.argv[1] beyond 20.So many.
    print "Result 'a' list is: ",rList
    print "The %s(th) 's length is: %d." % ( sys.argv[1],len(rList[-1]) )

if __name__=='__main__':
    main()
