#!/usr/bin/python
   
#EmailtoHIBP.py
#Author: Sudhanshu Chauhan - @Sudhanshu_C
     
#This Script will retrieve the Domain(s) at which the specified account has been compromised
#It uses the API provided by https://haveibeenpwned.com/
#Special Thanks to Troy Hunt - http://www.troyhunt.com/
#For MaltegoTransform library and Installation guidelines go to http://www.paterva.com/web6/documentation/developer-local.php

import sys
import urllib2
import json

from MaltegoTransform import *

HIBP = "https://haveibeenpwned.com/api/breachedaccount/"

mt = MaltegoTransform()
mt.parseArguments(sys.argv)
email = mt.getValue()
mt = MaltegoTransform()
getrequrl = HIBP + email

try:
    response = urllib2.urlopen(getrequrl)
    data = json.load(response)
    response = data
    for rep in response:
        mt.addEntity("maltego.Phrase","Pwned at " + rep)

except urllib2.URLError, e:  # "Response Codes" within https://haveibeenpwned.com/API/v1
    
    if e.code == 400:
        mt.addUIMessage("The e-mail account does not comply with an acceptable format",messageType="PartialError")
    
    if e.code == 404:
        UIMessage = email + " could not be found and has therefore not been pwned"
        mt.addUIMessage(UIMessage,messageType="Inform")
        
mt.returnOutput()