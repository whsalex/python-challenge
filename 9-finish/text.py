#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/good.html
# Un: huge     Pw: file

import Image,ImageDraw
import sys

SOURCE="page-source"

def usage():
    print '''
Usage: ./text.py INPUTFILE OUTPUTFILE
(IN/OUTPUT)File is the name of exist (PNG) file.
    '''


def checkArgv():
    argc=len(sys.argv)
    if argc != 3:
        usage()
	return 1

def main():
    if checkArgv():
        return -1
    inputfile=sys.argv[1]
    outputfile=sys.argv[2]

    first=""
    second=""
    flag=False

    fd=file(SOURCE,"r")
    lines=[line.strip() for line in fd.readlines()]
    fd.close()
    
    try:
        flist_start=lines.index('first:')
        flist_end=lines.index('second:')
        #print lines[flist_start+1:flist_end-1]
    
	slist_start=lines.index('second:')
        #print lines[slist_start+1:-2]
    except ValueError,e:
        print "Could not find the pattern.",e

    for i in range(flist_start+1,flist_end-1):
        first+=lines[i]

    #print "first: \n",first

    for i in lines[slist_start+1:-2]:
        second+=i
    #print "second: \n",second

    im=Image.open(inputfile)
    draw=ImageDraw.Draw(im)
    draw.line(eval(first))
    draw.line(eval(second))
    im.save(outputfile,"PNG")


if __name__=='__main__':
    main()
