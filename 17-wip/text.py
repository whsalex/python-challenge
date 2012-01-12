#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/romance.html
#The forth http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2,cookielib

URL='http://www.pythonchallenge.com/pc/return/romance.html'
cookieFile='cookies.file'

def usage():
    print '''
    Nothing.
    '''

def main():
    #Due to authenication
    passdomain=urllib2.HTTPPasswordMgrWithDefaultRealm()
    passdomain.add_password(None,URL,'huge','file')
    handler_au=urllib2.HTTPBasicAuthHandler(passdomain)

    #Handler the cookies
    cJar = cookielib.LWPCookieJar()
    handler_ck=urllib2.HTTPCookieProcessor(cJar)
  
    opener=urllib2.build_opener(handler_au,handler_ck)
    
    #opener.open
    urllib2.install_opener(opener)

    fp=urllib2.urlopen(URL)

    lines=[line for line in fp.readlines()]

    fp.close()

    #for li in lines:
    #    print li,

    print "cJar: ",cJar

    for int, cookie in enumerate(cJar):
        print "%d - %s" % (int, cookie)

    cJar.save(cookieFile)

if __name__=='__main__':
    main()
