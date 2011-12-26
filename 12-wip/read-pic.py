#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/evil.html

import Image

def usage():
    print '''
    Nothing.
    '''

def main():
   
    im=Image.open('evil2.gfx')

    x_max,y_max=im.size
    #print x_max,y_max
    
    for x in range(x_max):
        for y in range(y_max):
            pixel=im.getpixel((x,y))
            print pixel
    

if __name__=='__main__':
    main()
