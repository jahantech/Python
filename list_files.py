#!/usr/bin/python
from os import listdir
from os.path import isfile, join

mypath = "/root/"
#Script to list all the directories and files in given path

for files in listdir(mypath):
    if isfile(join(mypath,files)):
        print "File:", files
    else:
        print "Directory:", files
    
