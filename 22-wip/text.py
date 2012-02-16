#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/copper.html
#butter@fly - username:passwd

import Image

def usage():
    print '''
    Nothing.
    '''

def draw(pix_list):
    for i in range(len(pix_list)):
        print pix_list[i]

def run():
    #Will load gif module automatically
    gif=Image.open('white.gif')
    
    pixs=[]

    max_x,max_y=gif.size
    
    try:
        while True:
            #print gif.tell()

            #Check all the pixel and pick up all points not 0
            for x in range(max_x):
                for y in range(max_y):
                    pix=gif.getpixel((x,y))

                    if pix!=0:
                        #print "(%d,%d) is %d." % (x,y,pix)
                        pixs.append((x,y,pix))

            #Check next frames
            gif.seek(gif.tell()+1)
    except EOFError:
        #print "end of sequence/frame"
        pass

    draw(pixs)

def main():

    print "  ===  start level 22  === "
    run()
    print "  ===  finish level 22  === "

if __name__=='__main__':
    main()
