#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/idiot.html
#URL: http://www.pythonchallenge.com/pc/hex/idiot2.html
#butter@fly - username:passwd

import urllib,urllib2
import re,zipfile

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

def extractzipfile():
    zipf=zipfile.ZipFile('downloadfile')
    zipf.setpassword('redavni')
    zipf.extractall('/home/wanghs/practise/python/pcwork/20-wip/extrafloader')
    

def main():
    #Copy downloadfile from level 20
    #httpAuth()

    extractzipfile()

if __name__=='__main__':
    main()
