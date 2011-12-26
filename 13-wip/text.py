#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/disproportional.html

import Image

files={"0":"file1","1":"file2","2":"file3","3":"file4","4":"file5"}
string={"0":"","1":"","2":"","3":"","4":""}

def usage():
    print '''
    Nothing.
    '''

def main():
   
    fd=file('evil2.gfx','r')

    #lines=[line for line in fd.readlines()]
    lines=[line for line in fd.readlines()]
    fd.close()
 
    newfile=""
    for li in lines:
        newfile+=li

    #split
    for char in range(len(newfile)):
        string[str(char%5)]+=newfile[char]

    #Write to files
    for key in files:
        fd=file(files[key],"w")
        fd.write(string[key])
        fd.close()


if __name__=='__main__':
    main()
