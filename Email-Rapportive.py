#!/usr/bin/python

#Email-Rapportive.py
#Author: Sudhanshu Chauhan - @Sudhanshu_C

#Based upon the service Rapportive: http://www.rapportive.com/
#Credits: This code is based upon the research and code of Jordan Wright.
#Blog Link: http://jordan-wright.github.io/blog/2013/10/14/automated-social-engineering-recon-using-rapportive/
#Code Link: https://github.com/jordan-wright/rapportive
#This code requires the Requests library: https://pypi.python.org/pypi/requests/
#Rapportive Code: https://github.com/SudhanshuC/Rapportive/blob/master/rapportive.py
#For MaltegoTransform library and Installation guidelines go to http://www.paterva.com/web6/documentation/developer-local.php
  
from MaltegoTransform import *
import sys
import urllib2
import requests
mt = MaltegoTransform()
mt.parseArguments(sys.argv)
target_email=mt.getValue()
mt = MaltegoTransform()
random_email="random-email@gmail.com"
response = requests.get('https://rapportive.com/login_status?user_email=' + random_email).json()
profile = requests.get('https://profiles.rapportive.com/contacts/email/' + target_email, headers = {'X-Session-Token' : response['session_token']}).json()

if profile['contact']['name']:
  mt.addEntity("maltego.Person", profile['contact']['name'])

if profile['contact']['location']:
  mt.addEntity("maltego.Location", profile['contact']['location'])

if profile['contact']['occupations']:
  for occupation in profile['contact']['occupations']:
    mt.addEntity("maltego.Phrase", "Job Title: " + occupation['job_title'] + " at " + occupation['company'])

if profile['contact']['memberships']:
  for membership in profile['contact']['memberships']:
    purl=membership['profile_url']
    url=mt.addEntity("maltego.URL", membership['site_name'] + " profile: " + purl)
    url.addAdditionalFields("theurl","URL",True,purl)

mt.returnOutput()
