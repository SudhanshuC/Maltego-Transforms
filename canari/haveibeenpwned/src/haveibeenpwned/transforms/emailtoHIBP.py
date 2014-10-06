#!/usr/bin/env python

import sys
import urllib2

from canari.maltego.entities import EmailAddress, Phrase
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser

__author__ = 'Christian Heinrich'
__copyright__ = 'Copyright 2014, cmlh.id.au'
__credits__ = ['Sudhanshu Chauhan']

__license__ = 'GPL'
__version__ = '0.2'  # Incremented for canari 
__maintainer__ = 'Christian Heinrich'
__email__ = 'christian.heinrich@cmlh.id.au'
__status__ = 'Development'

__all__ = [
    'dotransform',
    'onterminate'
]

# Uncomment the line below if the transform needs to run as super-user
#@superuser

@configure(
    label='To Compromised Domains [haveibeenpwned]',
    description='Retrieves the Domain(s) at which the specified account has been compromised',
    uuids=[ 'cmlh.haveibeenpwned.emailtoHIBP' ],
    inputs=[ ( 'haveibeenpwned', EmailAddress ) ],
    remote=False,
    debug=False
)
def dotransform(request, response, config):

    HIBP = "https://haveibeenpwned.com/api/breachedaccount/"  # http://legacy.python.org/dev/peps/pep-0008/#constants
    
    email = request.value
    getrequrl = HIBP + email

    progress(50)
    
    try:
        urllib2_response = urllib2.urlopen(getrequrl)  # Renamed "response" due conflict within canari namespace 
        for rep in urllib2_response:
            e = Phrase("Pwned at %s" % rep)
            response += e
    except:
        print ""
        
    progress(100)

    return response


"""
Called if transform interrupted. It's presence is optional; you can remove this function if you don't need to do any
resource clean up.

TODO: Write your cleanup logic below or delete the onterminate function and remove it from the __all__ variable 
"""
def onterminate():
    debug('Caught signal... exiting.')
    exit(0)