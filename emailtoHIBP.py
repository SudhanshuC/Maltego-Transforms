#!/usr/bin/python
   
#EmailtoHIBP.py
#Author: Sudhanshu Chauhan - @Sudhanshu_C
     
#This Script will retrieve the Domain(s) at which the specified account has been compromised
#It uses the API provided by https://haveibeenpwned.com/
#Special Thanks to Troy Hunt - http://www.troyhunt.com/
#For MaltegoTransform library and Installation guidelines go to http://www.paterva.com/web6/documentation/developer-local.php
   
from MaltegoTransform import *
import sys
import urllib2
mt = MaltegoTransform()
mt.parseArguments(sys.argv)
email=mt.getValue()
mt = MaltegoTransform()
hibp="https://haveibeenpwned.com/api/breachedaccount/"
getrequrl=hibp+email
try:
response = urllib2.urlopen(getrequrl)
for rep in response:
mt.addEntity("maltego.Phrase","Pwned at " + rep)
except:
print ""
mt.returnOutput()

