#!/usr/bin/python


#Script to read xml and print values
from xml.dom import minidom

xmldoc = minidom.parse('testdata.xml')
listofitems = xmldoc.getElementsByTagName('item') 


for eachitem in listofitems :
    print "Name  : " , eachitem.getElementsByTagName("name")[0].firstChild.data
    print "Model : ", eachitem.getElementsByTagName("model")[0].firstChild.data
    print "Price : ", eachitem.getElementsByTagName("price")[0].firstChild.data
    print "******************"
