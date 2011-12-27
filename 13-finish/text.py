#!/usr/bin/env python
# URL: http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib

urlPhoneBook='http://www.pythonchallenge.com/pc/phonebook.php'

def usage():
    print '''
    Nothing.
    '''

def main():
    server=xmlrpclib.ServerProxy(urlPhoneBook)
    print server.system.listMethods()
    # ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
    print  server.phone('Bert')
    #'555-ITALY'

if __name__=='__main__':
    main()
