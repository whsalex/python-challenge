#!/usr/bin/env python
#URL: http://www.pythonchallenge.com/pc/hex/bonus.html
#butter@fly - username:passwd

import this

dict=this.d
oristr='va gur snpr bs jung?'

def usage():
    print '''
    Nothing.
    '''

def run():
    output=""

    for i in oristr:
        if i in dict:
            output+=dict[i]
        else:
            output+=i

    print "Out put is: %s." % output
    #print this.s

def main():

    print " That is the string of import this. \n"
    print "  ===  start level 22  === "
    run()
    print "  ===  finish level 22  === "

if __name__=='__main__':
    main()
