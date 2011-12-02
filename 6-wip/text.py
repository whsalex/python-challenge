#!/usr/bin/python2.6

import os
import pickle

filepath=os.path.join(os.path.abspath("."),"file")

fd=file(filepath,"r")
pickle_object=pickle.load(fd)
fd.close()

for line in pickle_object:
    word=""
    for sector in line:
        word+=sector[0]*sector[1]
    print word

