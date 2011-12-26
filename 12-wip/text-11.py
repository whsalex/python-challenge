#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/5808.html

import Image

#o: odd, e: even
imdic={'o_o':'im_odd_odd','e_e':'im_even_even','o_e':'im_odd_even',\
       'e_o':'im_even_odd','pix':'im_pix'}

def usage():
    print '''
    Nothing.
    '''
def chooseImage(x,y):
    if x%2==1 and y%2==1:
       return imdic['o_o']
    elif x%2==1 and y%2==0:
       return imdic['o_e']
    elif x%2==0 and y%2==1:
       return imdic['e_o']
    else:    # x%2==0 and y%2==0
       return imdic['e_e']

def main():
   
    im=Image.open('evil1.jpg')

    #init image
    for ims in imdic:
        imdic[ims]=Image.new("RGB",(640,480))
    
    x_max,y_max=im.size
    
    for x in range(x_max):
        for y in range(y_max):
            pixel=im.getpixel((x,y))
            #print pix
            chooseImage(x,y).putpixel((x,y),pixel)
            
            if pixel[0]%2==1 and pixel[1]%2==0 and pixel[2]==0:
                imdic['pix'].putpixel((x,y),pixel) 
    
    for ims in imdic:
        imdic[ims].save('%s.jpg' % ims,'JPEG')


if __name__=='__main__':
    main()
