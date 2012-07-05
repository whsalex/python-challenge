#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/italy.html

import Image

output='output.png'
outim=Image.new("RGB",(100,100))

def usage():
    print '''
    Nothing.
    '''

def drawPixel(x,y):
    
    antilist=range(x,y)
    antilist.reverse()
    
    #up line
    for temp_x in range(x,y):
        outim.putpixel((int(temp_x),x),pix_list.pop())

    #right line
    for temp_y in range(x,y):
        outim.putpixel((y,int(temp_y)),pix_list.pop())

    #down line
    for temp_x in antilist:
        outim.putpixel((int(temp_x),y),pix_list.pop())

    #left line
    for temp_y in antilist:
        outim.putpixel((x,int(temp_y)),pix_list.pop())

def main():
    im=Image.open('wire.png')
    
    x_max,y_max=im.size
    #print "x_max,y_max is (%s,%s)." % (x_max,y_max)

    global pix_list
    pix_list=[]

    for x in range(x_max):
        for y in range(y_max):
            pixel=im.getpixel((x,y))
	    #print pixel
	    pix_list.append(pixel)
   
    #From small to big
    #pix_list.sort()
    #reverse for pop. No needed,due to will pop last as first
    pix_list.reverse()

    indexList=range(100)

    while len(indexList) != 0:
        drawPixel(int(indexList[0]),int(indexList[-1]))

	#indexList.pop()
	#indexList.reverse()
	#indexList.pop()
	#indexList.reverse()
	indexList.pop()
	indexList.pop(0)

    #for x in range(100):
    #    for y in range(100):
    #        outim.putpixel((x,y),pixList.pop())

    outim.save(output,'PNG')


if __name__=='__main__':
    main()
