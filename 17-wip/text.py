#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/romance.html
#The forth http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2,cookielib,re
from os import linesep,unlink

URL='http://www.pythonchallenge.com/pc/return/romance.html'
PURL='http://www.pythonchallenge.com/pc/def/linkedlist.php'
NEWURL='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
tempoutputfile='tempoutput.txt'

BZ2String='BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

def usage():
    print '''
    Nothing.
    '''

def build_URL_opener():
    ''' 
    Add authority and cookies for open URL.But useless for this level...
    '''
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

def find_bzstring():
    '''
    Find and recoder the bz2 string.
    '''
#Comment due to useless by info of stage 17
#    fp1=urllib2.urlopen(URL)
#
#    lines=[line for line in fp1.readlines()]
#
#    #print "=======Stage 17======="
#    print fp1.info()
#    
#    fp1.close()

#By checking the headers of stage 4,find out should add busynothing (instaead of nothing)
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
    pattern2=re.compile('info=(.*?);')

    TEMPURL=NEWURL+"12345"
    infostring=""

    stopFlag=False

    try:
        unlink(tempoutputfile)
    except OSError,e:
        print "Create temp file",tempoutputfile
    
    #Find out the next link  
    while stopFlag==False:
 
        fp=urllib2.urlopen(TEMPURL)

        #Print the Set-Cookies header
        cookieHeader=fp.info().getheaders('Set-Cookie')
        print cookieHeader
        #Recorder the info 
        result=re.search(pattern2,cookieHeader[0])

        if result is not None:
            infostring+=result.groups()[0]
        #print "BZ2:",infostring
       
        #Find the next link
        for line in fp.readlines():
            print line

            nextone=re.search(pattern,line)

            if nextone is not None:
                #print nextone.groups()[0]
                TEMPURL=NEWURL+nextone.groups()[0]
                #Break after find the pattern
                break 
            
        #else for "for line in fp.readlines():"
        else:
            #Set stop flag when no pattern found
            stopFlag=True

        #Record the finding text
#        fd_tmp=file(tempoutputfile,'a')
#        fd_tmp.write(line+"%s" % linesep)
#        fd_tmp.write("".join(fp.info().getheaders('Set-Cookie'))+"%s" % linesep)
#        fd_tmp.close()

#        fp.close()
 
        print "="*50+"\n"*2

    print "BZ2 string is:",infostring

    #Recoder the result in tempfile
    fd_tmp=file(tempoutputfile,'a')
    fd_tmp.write("%s" % linesep)
    fd_tmp.write("BZ2 string is: ")
    fd_tmp.write(infostring+"%s" % linesep)
    fd_tmp.write("%s" % linesep)
    fd_tmp.close()

    BZ2String=infostring

def main():
    #build_URL_opener()
    
    #find_bzstring()
    print BZ2String

if __name__=='__main__':
    main()
