#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/ambiguity.html
#butter@fly - username:passwd

# Wrong!way is not white,white point is a wall.

import Image

def usage():
    print '''
    Nothing.
    '''

def getPixels():
    im=Image.open('maze.png')
    max_x,max_y=im.size
    #im.size is (641,641)

    pixlist={}

    for x in range(max_x):
        for y in range(max_y):
            pix=im.getpixel((x,y))
	    pixlist[(x,y)]=pix[0]

    fd=file('output','w')
    for i in pixlist:
        fd.write("%s : %s\n" % (i,pixlist[i]))
    fd.close()
    return pixlist


def getstart(list):
    '''
    Find the start point.
    Using yield/iter.
    '''

    for x in range(1,640):
        if list[(x,0)]==255:
            print "Start point (%s,0)." % x
            yield (x,0)

def testpoint(xy,pixlist,route):
    if pixlist[xy]==255:
        for i in route:
            if xy==i[0]:
                return False
        else:
            return True
    else:
        return False

def findnext(route,pixlist):
    '''
    Called by findway.
    Return success/fail flag,pervious route info(modified),new route info.
    '''
    #Search sequence is from down,left,right,top
    #Mark route in a list,like [((coord_x,coord_y),downflag,leftflag,rightflag,topflag)]

    oldpoint=route[-1]
    print "route.",
    for i in oldpoint:
        print i,

    print ""

    while True:
        if oldpoint[1]:
            #Try the below point
            if (oldpoint[0][1]+1<=640) and testpoint((oldpoint[0][0],oldpoint[0][1]+1),pixlist,route): 
                oldpoint[1]=False
                newpoint=[(oldpoint[0][0],oldpoint[0][1]+1),True,True,True,False]
                return True,oldpoint,newpoint
            else:
                oldpoint[1]=False
                continue
        elif oldpoint[2]:
            #Try the left point
            if (oldpoint[0][0]-1>=1) and testpoint((oldpoint[0][0]-1,oldpoint[0][1]),pixlist,route): 
                oldpoint[2]=False
                newpoint=[(oldpoint[0][0]-1,oldpoint[0][1]),True,True,False,True]
                return True,oldpoint,newpoint
            else:
                oldpoint[2]=False
                continue
        elif oldpoint[3]:
            #Try the right point
            if (oldpoint[0][0]+1<=639) and testpoint((oldpoint[0][0]+1,oldpoint[0][1]),pixlist,route): 
                oldpoint[3]=False
                newpoint=[(oldpoint[0][0]+1,oldpoint[0][1]),True,False,True,True]
                return True,oldpoint,newpoint
            else:
                oldpoint[3]=False
                continue
        elif oldpoint[4]:
            #Try the upper point
            if (oldpoint[0][1]-1>0) and testpoint((oldpoint[0][0],oldpoint[0][1]-1),pixlist,route): 
                oldpoint[4]=False
                newpoint=[(oldpoint[0][0],oldpoint[0][1]-1),False,True,True,True]
                return True,oldpoint,newpoint
            else:
                oldpoint[4]=False
                continue
        else:
            #Dead way.
            return False,oldpoint,oldpoint

def findway(coord,pixlist):
    #Search sequence is from down,left,right,top
    #Mark new point in a list,like [((coord_x,coord_y),downflag,leftflag,rightflag,topflag)]
    route=[]
    #add the startpoint to list
    route.append( [(coord[0],coord[1]),True,True,True,False] )

    while True:
        flag,oldpoint,newpoint=findnext(route,pixlist)

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
    pixlist=getPixels()

    #Search sequence is from down,left,right,top
    #Mark route in a list,like [((coord_x,coord_y),downflag,leftflag,rightflag,topflag)]

    success_flag=False

    while success_flag is not True:
        startpoints=getstart(pixlist)
    
        for i in startpoints:
            success_flag=findway(i,pixlist)
   
            if success_flag==True:
                break

        else:
            print "Cannot find a way to the bottom."
            break

def main():
    print "  ===  start level 24  === "
    run()
    print "  ===  finish level 24  === "

if __name__=='__main__':
    main()
