#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/idiot.html
#URL: http://www.pythonchallenge.com/pc/hex/idiot2.html
#butter@fly - username:passwd

#import xmlrpclib
import urllib,urllib2

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


def call_him():
    ''' Useless. '''
    #phoneServer=xmlrpclib.ServerProxy(urlPhoneBook)

    #List all method in server
    #print phoneServer.system.listMethods()

    #Call to mozart's father
    #print "==Get the number of mozart's fater.=="
    #print phoneServer.phone('Leopold')

    #Then find out the URL"http://www.pythonchallenge.com/pc/stuff/violin.php"
    #Just tell him "the flowers are on their way"
    saying="apologize"
    #saying="sorry"
    #saying="the flowers are on their way"
    words=urllib.quote_plus(saying)

    #Could see all http headers via "http://en.wikipedia.org/wiki/List_of_HTTP_header_fields"
    header={'Cookie':'info='+words}
    req=urllib2.Request(fatherAddr,headers=header)

    fp_final=urllib2.urlopen(req)
    lines=[line for line in fp_final.readlines()]
    fp_final.close()

    #Response from mozart's father
    print "==Response from mozart's father.=="
    for i in lines:
        print i,

def main():
    #call_him()
    #downloadFile('http://www.pythonchallenge.com/pc/hex/unreal.jpg','unreal.jpg')
    httpAuth()
    fd=urllib2.urlopen(URL_PIC)
    info=fd.info()
    #Find out the range hint.
    range_val=info.getheaders("Content-Range")
    print "Content-range header: %s" % range_val
    #It shows "Content-range header: ['bytes 0-30202/2123456789']"

#    #For check http headers. "http://en.wikipedia.org/wiki/List_of_HTTP_headers"
#    header={'Range':'bytes=30237-2123456789'}
#    req=urllib2.Request(URL_PIC,headers=header)
#
#    fp=urllib2.urlopen(req)
#    lines=[line for line in fp.readlines()]
#    print fp.info().getheaders("Content-Range")
#    fp.close()
#
#    for i in lines:
#        print i,
    

if __name__=='__main__':
    main()
