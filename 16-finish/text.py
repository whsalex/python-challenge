#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/mozart.html

import Image
import re

output='output.gif'
outim=Image.new("RGB",(640,480))

def usage():
    print '''
    Nothing.
    '''

def main():
    im=Image.open('mozart.gif')
    
    x_max,y_max=im.size

    for y in range(y_max):
        #Flag for line movement
        moveFlag=False

	if moveFlag==False:
            for x in range(x_max-4):
                pixel=im.getpixel((x,y))

	        #Find the purple line
	        if pixel==im.getpixel((x+1,y))==im.getpixel((x+2,y))\
			        ==im.getpixel((x+3,y))==im.getpixel((x+4,y))\
			        ==195:
		    for tmp_x in range(x_max):
			#Make a move when found the pattern(purple line)
			# coord_x = (tmp_x+640-x)%640    equal
			# tmp_x -x    when   tmp_x > x
			# 640-(x-tmp_x)   when   tmp_x < x
			coord_x=(tmp_x+640-x)%640
			newpixel=im.getpixel((tmp_x,y))
		        outim.putpixel((coord_x,y),newpixel)
		    moveFlag=True
		#else:
		#    pass

        #MoveFlag=True means already moved
	#else:
	#    continue
    
    outim.save(output,'GIF')


if __name__=='__main__':
    main()
