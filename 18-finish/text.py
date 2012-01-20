#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/balloons.html

import urllib,urllib2
import difflib
import gzip
from os import linesep
#import Image

URL_domain='http://www.pythonchallenge.com'
URL='http://www.pythonchallenge.com/pc/return/balloons.html'
#Difference is brightness
NEWURL='http://www.pythonchallenge.com/pc/return/brightness.html'
URL_JPG='http://www.pythonchallenge.com/pc/return/balloons.jpg'
URL_GZ='http://www.pythonchallenge.com/pc/return/deltas.gz'

def usage():
    print '''
    Nothing.
    '''

#def httpAuth():
#    passDomain=urllib2.HTTPPasswordMgrWithDefaultRealm()
#    passDomain.add_password(None,URL_domain,'huge','file')
#    hander_au=urllib2.HTTPBasicAuthHandler(passDomain)
#    opener=urllib2.build_opener(hander_au)
#    urllib2.install_opener(opener)

def downloadFile(url,name):
    '''
    Download file from 'http://www.pythonchallenge.com/pc/return/balloons.jpg',huge@file.
    '''
    urllib.urlretrieve(url,name)
   
#def newPixel(one,two):
#    return one-two
# 
#def createNew():
#    '''
#    Useless... since the difference is "brightness"
#    '''
#    fd=Image.open('balloons.jpg')
#    max_x,max_y=fd.size
#    #print max_x,max_y
#    #Size is (750,335)
#
#    newfd=Image.new('RGB',(375,335))
#
#    for x in range(375):
#        for y in range(max_y):
#            minus=map(newPixel,fd.getpixel((x,y)),fd.getpixel((x+375,y)))
#            print fd.getpixel((x,y)),fd.getpixel((x+375,y))
#            newfd.putpixel((x,y),tuple(minus))
#
#    newfd.save('new.jpg','JPEG')

def main():
    #Below is useless...
    #Download the jpg file -> balloons.jpg
    #downloadFile()
    #createNew()
    #httpAuth()

    #Download the file "deltas.gz"  huge@file
    #downloadFile(URL_GZ,'deltas.gz')

    fd=gzip.open('deltas.gz','r')
    lines=[line.strip() for line in fd.readlines()]
    fd.close()

    #Find out the center line,it should be 53-55 
    #print lines[0].index("   ")

    list_a=[]
    list_b=[]

    #Divide into two list
    for line in lines:
        list_a.append(line[:53])
        list_b.append(line[56:])

    diff=difflib.Differ()

    result=list(diff.compare(list_a,list_b))

    file=["","",""]
 
    for line in result:
        newlist=[chr(int(block,16)) for block in line[2:].split( )]
        #print newlist
        newline="".join(newlist)

        if line.startswith("- "):
            file[0]+=newline
        elif line.startswith("+ "):
            file[1]+=newline
        #No option "? ' - "line not present in either input sequence"
        elif line.startswith("  "):
            file[2]+=newline
        else:
            print "error diff."
            exit(1)

    for i in range(len(file)):
        open("pic%s.png" % (i),"w").write(file[i])

if __name__=='__main__':
    main()
