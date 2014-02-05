#!/usr/bin/python
 
#phntocomp.py
#Author: Sudhanshu Chauhan - @Sudhanshu_C
 
#This Script will retrieve the Company name from the provided Phone Number
#It uses the API provided by https://www.opencnam.com
 
from MaltegoTransform import *
import sys
import urllib2
mt = MaltegoTransform()
mt.parseArguments(sys.argv)
phn=mt.getValue()
phn=phn.replace(' ','')
mt = MaltegoTransform()
opencnam="https://api.opencnam.com/v2/phone/"
getrequrl=opencnam+phn
response = urllib2.urlopen(getrequrl)
mt.addEntity("maltego.Phrase", response.read())
mt.returnOutput()
