#!/usr/bin/env python

# This script prints out a JSON array of the Alexa top 500 sites for the country
# passed in as the first command-line argument, using a 2-letter code (e.g. CN)
#
# It requires the requests and lxml packages:
#
#   pip install requests
#   pip install lxml

import sys
import requests
import lxml.html

print "["
for i in range(0,21):
    html = requests.get("http://www.alexa.com/topsites/countries;%d/%s" % (i, sys.argv[1].upper())).content
    dom = lxml.html.fromstring(html)
    
    for link in dom.cssselect('.site-listing .desc-paragraph a'):
        print '"%s",' % link.text_content()

print "]"   