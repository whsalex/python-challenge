#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/ambiguity.html
#butter@fly - username:passwd

import Image,time

def usage():
    print '''
    Nothing.
    '''

def getPixels():
    im=Image.open('maze.png')
    max_x,max_y=im.size
    #im.size is (641,641)

    plist={}

    for x in range(max_x):
        for y in range(max_y):
            pix=im.getpixel((x,y))
	    plist[(x,y)]=(pix[0],pix[1],pix[2])

    fd=file('output','w')
    for i in plist:
        fd.write("%s : %s\n" % (i,plist[i]))
    fd.close()
    return plist


def getstart(list):
    '''
    Find the start point.
    Using yield/iter.
    Useless....  due to start point is (639,0)
    '''

    for x in range(1,640):
        # 255, 255, 255  mean white point.
        # Only R in RGB = 255 is not equal white.
        if list[(x,0)]==255:
            print "Start point (%s,0)." % x
            yield (x,0)

def testpoint(xy,route):
    if pixlist[xy][0]!=255 or pixlist[xy][1]!= 255 or pixlist[xy][2]!=255:
        # Check whether the point appeared or not.
        for i in route:
            if xy==i[0]:
                return False
        return True
    else:
        return False

def findnext(route):
    '''
    Called by findway.
    Return success/fail flag,pervious route info(modified),new route info.
    '''
    #Search sequence is from down,left,right,top
    #Mark route in a list,like [((coord_x,coord_y),downflag,leftflag,rightflag,topflag)]

    oldpoint=route[-1]
    #print "route.",
    #for i in oldpoint:
    #    print i,
    #print ""

    while True:
        if oldpoint[1]:
            oldpoint[1]=False
            #Try the below point
            if (oldpoint[0][1]+1<=640) and testpoint((oldpoint[0][0],oldpoint[0][1]+1),route): 
                newpoint=[(oldpoint[0][0],oldpoint[0][1]+1),True,True,True,False]
                return True,oldpoint,newpoint
            else:
                # break the if - else,and retry in next loop
                continue
        elif oldpoint[2]:
            oldpoint[2]=False
            #Try the left point
            if (oldpoint[0][0]-1>=1) and testpoint((oldpoint[0][0]-1,oldpoint[0][1]),route): 
                newpoint=[(oldpoint[0][0]-1,oldpoint[0][1]),True,True,False,True]
                return True,oldpoint,newpoint
            else:
                # break the if - else,and retry in next loop
                continue
        elif oldpoint[3]:
            oldpoint[3]=False
            #Try the right point
            if (oldpoint[0][0]+1<=640) and testpoint((oldpoint[0][0]+1,oldpoint[0][1]),route): 
                newpoint=[(oldpoint[0][0]+1,oldpoint[0][1]),True,False,True,True]
                return True,oldpoint,newpoint
            else:
                # break the if - else,and retry in next loop
                continue
        elif oldpoint[4]:
            oldpoint[4]=False
            #Try the upper point
            if (oldpoint[0][1]-1>=1) and testpoint((oldpoint[0][0],oldpoint[0][1]-1),route): 
                newpoint=[(oldpoint[0][0],oldpoint[0][1]-1),False,True,True,True]
                return True,oldpoint,newpoint
            else:
                # break the if - else,and retry in next loop
                continue
        else:
            # No other choice for this point. Dead way.
            return False,oldpoint,oldpoint

def findway(coord):
    #Search sequence is from down,left,right,top
    #Mark new point in a list,like [((coord_x,coord_y),downflag,leftflag,rightflag,topflag)]
    route=[]
    #add the startpoint to list
    route.append( [(coord[0],coord[1]),True,True,True,False] )

    while True:
        flag,oldpoint,newpoint=findnext(route)

        if flag is not True:
            #Could not find next point,need back to pervious point
            route.pop()
            if len(route)==0:
                #No point exist in list,dead startpoint
                print "Dead start point."
                return False

        else:
            #Could find next point,continue to try
            #Modify the old point
            route.pop()
            route.append(oldpoint)
            #Add the new point
            route.append(newpoint)

            if newpoint[0][1] == 640:
                #Reach the bottom,it succeed
                #Route list is the point of the maze
                #Route is the right way
                print "Find a way."
                for i in route:
                    print i[0]
                return True

def run():
    global pixlist
    pixlist=getPixels()

    #Search sequence is from down,left,right,top
    #Mark route in a list,like [((coord_x,coord_y),downflag,leftflag,rightflag,topflag)]

    #Start point is fixed,not white point.(639,0)
    startpoint=(639,0)
   
    success_flag=findway(startpoint)
   
    if success_flag!=True:
       print "Cannot find a way from (639,0) to the bottom."
    else:
       print "done"

def main():
    print "  ===  start level 24  === "
    start_time=time.time()
    run()
    finish_time=time.time()
    print "Program running for %d seconds." % ( finish_time - start_time ) 
    print "  ===  finish level 24  === "

if __name__=='__main__':
    main()
