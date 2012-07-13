#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/copper.html
#butter@fly - username:passwd

import Image,ImageDraw

def usage():
    print '''
    Nothing.
    '''

def draw(pix_list):
    #for i in range(len(pix_list)):
    #    print pix_list[i]

    #calc how many characters exist
    nchar=pix_list.count((100,100))
    
    im=Image.new('RGB',(nchar*200,200))
    fd=ImageDraw.Draw(im)

    #coord=(75,75)
    #Since first coord is (100,100)
    count_char=-1

    for point in pix_list:
        if point == (98,98):
            temp_coord=(coord[0]-10, coord[1]-10)
        elif point == (98,100):
            temp_coord=(coord[0]-10, coord[1])
        elif point == (98,102):
            temp_coord=(coord[0]-10, coord[1]+10)
        elif point == (100,98):
            temp_coord=(coord[0], coord[1]-10)
        elif point == (100,100):
            #new character
            count_char+=1
            coord=(75+(count_char*200),75)
            continue
        elif point == (100,102):
            temp_coord=(coord[0], coord[1]+10)
        elif point == (102,98):
            temp_coord=(coord[0]+10, coord[1]-10)
        elif point == (102,100):
            temp_coord=(coord[0]+10, coord[1])
        elif point == (102,102):
            temp_coord=(coord[0]+10, coord[1]+10)
        else:
            print "Error coordinate"
            return
        
        fd.line((coord,temp_coord))
        coord=temp_coord
    
    im.save('output.png')
    print " Output file is: output.png  "

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
                        #Actual "pix==8"
                        pixs.append((x,y))

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
