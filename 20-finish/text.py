#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/idiot.html
#URL: http://www.pythonchallenge.com/pc/hex/idiot2.html
#butter@fly - username:passwd

#import xmlrpclib
import urllib,urllib2
import re,zipfile

#urlPhoneBook='http://www.pythonchallenge.com/pc/phonebook.php'
#fatherAddr='http://www.pythonchallenge.com/pc/stuff/violin.php'
URL_domain='http://www.pythonchallenge.com/pc/hex'
URL_PIC='http://www.pythonchallenge.com/pc/hex/unreal.jpg'

def usage():
    print '''
    Nothing.
    '''

def httpAuth():
    '''Using urllib2.Or using urllib open "http://usrname:passwd@url"'''
    passDomain=urllib2.HTTPPasswordMgrWithDefaultRealm()
    passDomain.add_password(None,URL_domain,'butter','fly')
    hander_au=urllib2.HTTPBasicAuthHandler(passDomain)
    opener=urllib2.build_opener(hander_au)
    urllib2.install_opener(opener)

def downloadFile(url,name):
    '''
    Download file from 'http://www.pythonchallenge.com/pc/hex/unreal.jpg',butter@fly
    '''
    urllib.urlretrieve(url,name)


def loop_front():
    fp=urllib2.urlopen(URL_PIC)
    info=fp.info()
    #Find out the range hint.
    range_val=info.getheaders("Content-Range")
    fp.close()
    print "Initial content-range header: %s" % range_val
    #It shows "Content-range header: ['bytes 0-30202/2123456789']"

    #Findout the pattern of string
    pattern=re.compile("bytes \d*-(\d*)/\d*")
    result=re.search(pattern,range_val[0])

    if result is not None:
        endrange=int(result.groups()[0])
        #print "Initial end range is: ",endrange
        #Need to find out next message

    # After tried to 2123456789. Found 30346 is the limit range.
    while endrange<=2123456789:
        #For check http headers. "http://en.wikipedia.org/wiki/List_of_HTTP_headers"
        header={'Range':'bytes='+str(endrange+1)+'-2123456789'}
        req=urllib2.Request(URL_PIC,headers=header)

        try:
            fp=urllib2.urlopen(req)
        except urllib2.HTTPError,e:
            print "Reason is out of range - %s.Endrange now is %d." % (e,endrange)
            break

        #fp=urllib2.urlopen(req)
        lines=[line for line in fp.readlines()]

        info=fp.info()
        range_val=info.getheaders("Content-Range")
        #print "content-range header: %s" % range_val

        fp.close()

        for li in lines:
            print li,

        result=re.search(pattern,range_val[0])

        if result is not None:
            endrange=int(result.groups()[0])

def loop_back():
    #Find the area from the backdoor
    startrange=2123456789
    while startrange>30346:
        header={'Range':'bytes='+str(startrange)+'-2123456789'}
        req=urllib2.Request(URL_PIC,headers=header)

        try:
            fp=urllib2.urlopen(req)
        except urllib2.HTTPError,e:
            print "Reason is out of range - %s.Startrange now is %d." % (e,startrange)
            break

        lines=[line for line in fp.readlines()]
        fp.close()

        for li in lines:
            print li,

        startrange-=1

def download_zipfile():
    '''
    Got the message: 
    1. the password is your new nickname in reverse.
    2. and it is hiding at 1152983631.
    '''

    header={'Range':'bytes=1152983631-2123456789'}
    req=urllib2.Request(URL_PIC,headers=header)

    fd=file("downloadfile","w")
    fp=urllib2.urlopen(req)

    for li in fp:
        fd.write(li)

    fp.close()
    fd.close()

def extractzipfile():
    zipf=zipfile.ZipFile('downloadfile')
    zipf.setpassword('redavni')
    zipf.extractall('./extrafloader')
    

def main():
    #downloadFile('http://www.pythonchallenge.com/pc/hex/unreal.jpg','unreal.jpg')
    httpAuth()

    #loop_front()

    #loop_back()

    #download_zipfile()
    
    extractzipfile()

if __name__=='__main__':
    main()
