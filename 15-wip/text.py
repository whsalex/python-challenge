#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/uzi.html

import calendar
import re

pattern=re.compile("\n25 26 27 28 29 30 31\n")

def usage():
    print '''
    Nothing.
    '''

def main():
    ncal=calendar.TextCalendar()
   
    ylist=range(10)
    ylist.insert(0,"")

    years=[]

    #in case have year like 196
    for a in ylist:
        for b in range(10):
	    tempyear="1"+str(a)+str(b)+"6"

            #Only calc the 4 year,since 29 days in Feb
            if int(tempyear)%4 == 0:
                #ncal.prmonth(int(tempyear),1)
                #print ncal.formatmonth(int(tempyear),1)
                image=ncal.formatmonth(int(tempyear),1)
		result=re.search(pattern,image)

		if result is not None:
                    years.append(tempyear)
                    #print image

    print years

if __name__=='__main__':
    main()
