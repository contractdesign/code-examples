#!/usr/bin/env python3
# coding: utf-8



import requests
import bs4


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#
# retrieve a dictionary of details for the specified WARN
#
def get_WARN_details(url):
    """Given the URL for a specific WARN, parse the page and return some of the fields
    in a dictionary"""
    page = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(page.content.decode('utf-8','ignore'), features="html.parser")
    
    d_details = {}
    for p in soup.find_all('p'):
        contents = p.contents[0]
        
        for s in ['Date of Notice', 'Business Type', 'Classification', 'Number Affected',
                  'Reason for Dislocation', 'Layoff Date']:
            if contents.startswith(s):
                try:
                    key, _, value = contents.partition(':')
                    d_details[key] = value.strip()
                except:
                    d_details[key] = None

    return d_details

#
# process all of the WARN acts on that url
#
def get_WARN(l_fields, basename='https://labor.ny.gov/app/warn/'):
    """Parse the main WARN webpage and return a list of dictionary containing each WARN's data"""
    page = requests.get(basename, headers=headers)
    l_warn = []
    
    # for utf-8 decoding, see https://stackoverflow.com/questions/7219361/python-and-beautifulsoup-encoding-issues
    soup = bs4.BeautifulSoup(page.content.decode('utf-8','ignore'), features="html.parser")
      
    # print CSV header
    for key in l_fields:
        if key==l_fields[-1]:
            end = '\n'
        else:
            end = '|'
        print(key, end=end)
        
    # get all of the a tags on the page and filter for those that
    # contain 'details.asp'        
    for a in soup.find_all('a', href=True):
        if 'details.asp' in a['href']:
            text = a.contents[0].get_text()
            d_company = {}
            try:
                
                company, _, region = text.partition(' - ')
                url = basename + a['href']
                details = get_WARN_details(url)

                data = {'company': company, 'region': region,
                               'url': basename+a['href']}
                for key in details.keys():
                    data[key] = details[key]
                
                try:
                    for key in l_fields:
                        if key==l_fields[-1]:
                            end = '\n'
                        else:
                            end = '|'
                        print(data[key], end=end)
                except:
                    pass
                l_warn.append(data)
                
            except:
                pass
    return l_warn
                
get_WARN(l_fields=['Date of Notice', 'Business Type', 'region', 'company', 'Number Affected', 'Layoff Date', 'Reason for Dislocation', 'Classification'])

        
    


# # Example fields in WARN details
# 
# ```
# Date of Notice: 3/19/2020
# Event Number: 2019-1553
# Rapid Response Specialist: Stuart Goldberg
# Reason Stated for Filing: Temporary Plant Layoff
# Company:
# County: New York/Kings | WDB Name: NEW YORK CITY | Region: New York City
# Contact: Kimberly Colón-Möller, Vice President of Human Resources
# Phone: (917) 207-0788
# Business Type: Catering
# Number Affected: 689 (total number affected for all sites)
# Total Employees: -----
# Layoff Date: Layoffs began on 3/14/2020.
# Closing Date: -----
# Reason for Dislocation: Unforeseeable business circumstances prompted by COVID-19
# FEIN NUM: 46-3563279
# Union: The employees are not represented by a union.
# Classification: Temporary Plant Layoff
# <strong>Affected Maison Kayser, LLC sites:</strong>
# 1294 3rd Avenue, New York, NY 10021 (52 affected employees) 
# ``` 
# 
# 

# In[ ]:




