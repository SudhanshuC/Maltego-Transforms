#!/usr/bin/python
 
#reverseipdomain.py
#Author: Sudhanshu Chauhan - @Sudhanshu_C
 
#This Script will perform a reverse IP domain check
#http://www.yougetsignal.com
 
from MaltegoTransform import *
import sys
import urllib2
import re
from os.path import exists
mt = MaltegoTransform()
mt.parseArguments(sys.argv)
url=mt.getValue()
mt = MaltegoTransform()
opencnam="http://domains.yougetsignal.com/domains.php?remoteAddress="
getrequrl=opencnam+url
header={'User-Agent':'Mozilla',}
req=urllib2.Request(getrequrl,None,header)

if exists('reverseipdomainop.txt'):
  flt=open('reverseipdomainoptemp.txt','wr')
  data=flt.read()
  for d in data:
    mt.addEntity("maltego.Domain", d)

else:
  response = urllib2.urlopen(req)
  domains =re.findall("((?:[0-9]*[a-z][a-z\\.\\d\\-]+)\\.(?:[0-9]*[a-z][a-z\\-]+))(?![\\w\\.])",response.read())
  fl=open('reverseipdomainop.txt','a')
  flt=open('reverseipdomainoptemp.txt','a')
  for domain in domains:
    fl.write(domain)
    mt.addEntity("maltego.Domain", domain)

mt.returnOutput()
