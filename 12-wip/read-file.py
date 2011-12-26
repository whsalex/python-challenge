#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/evil.html

import Image

def usage():
    print '''
    Nothing.
    '''

def main():
   
    fd=file('evil2.gfx','r')

    lines=[line.strip() for line in fd.readlines()]

    for i in lines:
        print i

if __name__=='__main__':
    main()
