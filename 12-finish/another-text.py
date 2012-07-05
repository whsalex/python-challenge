#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/evil.html

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

    for f_no in files:
        files[f_no]=file(files[f_no],'w')

    temp_count=0
    for i in newfile:
        files[str(temp_count)].write(i)
        temp_count=(temp_count+1)%5

    for f_no in files:
        files[f_no].close()

if __name__=='__main__':
    main()
