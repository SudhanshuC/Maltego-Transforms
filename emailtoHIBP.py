#!/usr/bin/python
   
#EmailtoHIBP.py
#Author: Sudhanshu Chauhan - @Sudhanshu_C
     
#This Script will retrieve the Domain(s) at which the specified account has been compromised
#It uses the API provided by https://haveibeenpwned.com/
#Special Thanks to Troy Hunt - http://www.troyhunt.com/
#For MaltegoTransform library and Installation guidelines go to http://www.paterva.com/web6/documentation/developer-local.php

import sys  # PEP 8 http://legacy.python.org/dev/peps/pep-0008/#imports
import urllib2

from MaltegoTransform import *

HIBP = "https://haveibeenpwned.com/api/breachedaccount/" # PEP 8 http://legacy.python.org/dev/peps/pep-0008/#constants

mt = MaltegoTransform()
mt.parseArguments(sys.argv)
email = mt.getValue()  # PEP 8 http://legacy.python.org/dev/peps/pep-0008/#other-recommendations
mt = MaltegoTransform()
getrequrl = HIBP + email

try:
    response = urllib2.urlopen(getrequrl)
    for rep in response:
        mt.addEntity("maltego.Phrase","Pwned at " + rep)

except:
        print ""
        
mt.returnOutput()