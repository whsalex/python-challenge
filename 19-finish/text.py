#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/bin.html
#butter@fly - username:passwd

import urllib2
import base64,binascii
import wave
from os import unlink

URL_domain='http://www.pythonchallenge.com'
URL='http://www.pythonchallenge.com/pc/hex/bin.html'

def usage():
    print '''
    Nothing.
    '''

def httpAuth():
    passDomain=urllib2.HTTPPasswordMgrWithDefaultRealm()
    passDomain.add_password(None,URL_domain,'butter','fly')
    hander_au=urllib2.HTTPBasicAuthHandler(passDomain)
    opener=urllib2.build_opener(hander_au)
    urllib2.install_opener(opener)

def getText():
    httpAuth()

    fp=urllib2.urlopen(URL)
    lines=[line.strip() for line in fp.readlines()]
    fp.close()

    code=lines[27:-4]
    return code

def createWav():
    str_list=getText()
    string="".join(str_list)
   
    #Create a media file,which speak "sorry"
    fd=file("indian.wav","w")
    fd.write(base64.b64decode(string))
    #fd.write(binascii.a2b_base64(newstr))
    fd.close()

def endianRevert():
    '''Reference from google.'''
    wd_old=wave.open("indian.wav","rb")
    params=wd_old.getparams()
    print params

    try:
        unlink("enddian.wav")
    except OSError:
        print "Generate output file."
    else:
        print "Update output file."

    wd_new=wave.open("enddian.wav","wb")
    wd_new.setparams(params)
    
    #Google...need to reverse by frames.I did it all reverse.....
    for i in range(params[3]):
        wd_new.writeframes(wd_old.readframes(1)[::-1])

    wd_old.close()
    wd_new.close()

def main():
    #createWav()
    endianRevert()
    #Getting stuck... google find answer. Need reverse


if __name__=='__main__':
    main()
