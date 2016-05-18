#!/usr/bin/env python2.7

#
# script to print the companies mentioned recently on thelayoff.com
#

import requests, bs4

url = "https://www.thelayoff.com/last-25.php"
res = requests.get( url )
soup = bs4.BeautifulSoup( res.text, "lxml" )

d_company = {}

# get all of the links within div with the class of "context"
for item in soup.select( 'div[class="context"] > a' ):
    # the name of the company is the href link
    name_company = item.get('href')[1:]

    if name_company in d_company:
        d_company[name_company] = d_company[name_company] + 1
    else:
        d_company[name_company] = 1


for company in sorted(d_company.keys()):
    print "%0.25s:\t%s" %(company, d_company[company])
    

