#!/usr/bin/python

__author__ = 'An Yu <an@an-yu.net>'

import sys, os
import urllib, re, urlparse
from bs4 import BeautifulSoup

desktop_folder = os.path.expanduser('~/Desktop/roundup_images')
number = [0]

def get_image(link):

    os.mkdir (desktop_folder)

    weblink = urllib.urlopen(link)
    soup = BeautifulSoup(weblink)

    for i in soup.findAll('img', attrs={'src': re.compile('(?i)(jpg\??)[0-9]*$')}):
        full_url = urlparse.urljoin(link, i['src'])
        if full_url.find("thumbnail"):
            full_url = full_url.replace("thumbnail", "original")
            print "Campaign Original Image: ", full_url
            number = 0
            urllib.urlretrieve(full_url, os.path.join(desktop_folder, 'image%d.jpg' % number))
            number = number+1
            break

def main():
    
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: ./RoundupImages.py <campaignURL>\n")
        sys.exit(-1)
    
    campaignURL = sys.argv[1]
    get_image(campaignURL)
    
if __name__ == '__main__':
    main()
    sys.exit(0)