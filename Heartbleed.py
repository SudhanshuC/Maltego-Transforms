#!/usr/bin/python
from MaltegoTransform import *
import sys
import urllib2
import re
mt = MaltegoTransform()
mt.parseArguments(sys.argv)
domain=mt.getValue()
url="http://safeweb.norton.com/heartbleed?url=www."
getrequrl=url+domain
try:
  response = urllib2.urlopen(getrequrl)
  ser=re.search(r'is vulnerable',response.read())
  if ser:
    print "a"
    mt.addEntity("maltego.Phrase","HeartBleed Vulnerable")
except:
  print ""
mt.returnOutput()
