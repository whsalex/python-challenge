#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/romance.html
#The forth http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2,cookielib,re

URL='http://www.pythonchallenge.com/pc/return/romance.html'
PURL='http://www.pythonchallenge.com/pc/def/linkedlist.php'
NEWURL='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing'
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

#Comment due to useless by info of stage 17
#    fp1=urllib2.urlopen(URL)
#
#    lines=[line for line in fp1.readlines()]
#
#    #print "=======Stage 17======="
#    print fp1.info()
#    
#    fp1.close()

#By checking the headers of stage 4,find out should add busynothing
#    fp2=urllib2.urlopen(PURL)
#
#    plines=[line for line in fp2.readlines()]
#
#    print "=======Stage 4======="
#    infos=fp2.info()
#    print infos
#    print "===Set-Cookies==="
#    print infos.getheader('Set-cookie')
#    
#    fp2.close()

    pattern=re.compile('and the next busynothing is (\d+)')

    TEMPURL=NEWURL
    stopFlag=False
    
    #Find out the next link  
    while stopFlag==False:
 
        fp=urllib2.urlopen(TEMPURL)

        for line in fp.readlines():
            nextone=re.match(pattern,line)

            if nextone is not None:
                print line
                #print nextone.groups()[0]
                TEMPURL=NEWURL+"="+nextone.groups()[0]
            else:
                print line
                stopFlag=True

        fp.close()




if __name__=='__main__':
    main()
