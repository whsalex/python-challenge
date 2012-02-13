#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/idiot.html
#URL: http://www.pythonchallenge.com/pc/hex/idiot2.html
#butter@fly - username:passwd

#Failed to solve it...... Searching idea form baidu.

import zipfile
import zlib,bz2

def usage():
    print '''
    Nothing.
    '''

def extractzipfile():
    zipf=zipfile.ZipFile('downloadfile')
    zipf.setpassword('redavni')
    zipf.extractall('./file.bk')
    
def run():
    fd=file("./file.bk/package.pack","r")
    lines=[line for line in fd.readlines()]
    fd.close()

    strings="".join(lines)

    output_str=""

    stop_flag=False
    skip_zlib=False
    skip_bz2=False
    skip_reverse=False

    while not stop_flag:

        #Try to extract via zlib. Mark " " when success.
        if not skip_zlib:
            try:
                strings=zlib.decompress(strings)
                output_str+=" "
                #Reset bz2 and reverse flag when success.
                skip_bz2=False
                skip_reverse=False
                continue
            except zlib.error,e:
                #print "Zlib extract fail. Reason is: %s " % e
                skip_zlib=True
                continue

        #Try to extract via bz2. Mark "#" when success.
        if not skip_bz2:
            try:
                strings=bz2.decompress(strings)
                output_str+="#"
                #Reset zlib and reverse flag when success.
                skip_zlib=False
                skip_reverse=False
                continue
            except IOError,e:
                #print "bz2 extract fail. Reason is: %s " % e
                skip_bz2=True
                continue

        #Reverse strings when fail to 
        if not skip_reverse:
            #print "Reverse.\n"
            strings=strings[::-1]
            skip_reverse=True
            skip_zlib=False
            skip_bz2=False
            output_str+="\n"
            continue

        #All skip,setting stop flag.
        stop_flag=True
   
    #End while loop
    print output_str

def main():
    #Copy downloadfile from level 20
    #extractzipfile()
    
    print " "
    run()
    print " "

if __name__=='__main__':
    main()
