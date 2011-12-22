#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/5808.html

import Image

def usage():
    print '''
    Nothing.
    '''

def checkArgv():
    pass

def main():
   
    im=Image.open('cave.jpg')
    im1=Image.new("RGB",(640,480))
    
    x_max,y_max=im.size
    
    for x in range(x_max):
        for y in range(y_max):
            pix=im.getpixel((x,y))
            #print pix
            if pix[0]%2==1 and pix[1]%2==0 and pix[2]==0:
                im1.putpixel((x,y),pix) 
    im1.save('output.jpg',"JPEG")


if __name__=='__main__':
    main()
