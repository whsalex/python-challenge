#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/evil.html

import Image

def usage():
    print '''
    Nothing.
    '''

def main():
   
    im=Image.open('evil1.jpg')
    im1=Image.new("RGB",(640,480))

    x_max,y_max=im.size
    #print x_max,y_max
    
    for x in range(x_max):
        for y in range(y_max):
            pixel=im.getpixel((x,y))
            #print pixel

            #if pixel[0]!=0 and pixel[1]!=0 and pixel[2]!=0:
            #    im1.putpixel((x,y),pixel)
            plist=list(pixel)
            for pix in range(len(plist)):
                    plist[pix]+=50
            
            im1.putpixel((x,y),tuple(plist))
                

    im1.save('result.jpg','jpeg')
    
    #for ims in imdic:
    #    imdic[ims].save('%s.jpg' % ims,'JPEG')

if __name__=='__main__':
    main()
