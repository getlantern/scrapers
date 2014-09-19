#!/usr/bin/env python

# This script prints out a JSON array of the Alexa top 500 sites in China.
#
# It requires the requests and lxml packages:
#
#   pip install requests
#   pip install lxml

import requests
import lxml.html

print "["
for i in range(0,21):
    html = requests.get("http://www.alexa.com/topsites/countries;%d/CN" % i).content
    dom = lxml.html.fromstring(html)
    
    for link in dom.cssselect('.site-listing .desc-paragraph a'):
        print '"%s",' % link.text_content()

print "]"   