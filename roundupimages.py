#!/usr/bin/python

__author__ = 'An Yu <an@an-yu.net>'

import sys, os
import urllib, re, urlparse
from bs4 import BeautifulSoup

desktop_folder = os.path.expanduser('~/Desktop/roundup_images')
number = 0

def get_image(link):
    global number
    if not os.path.exists(desktop_folder):
        os.mkdir (desktop_folder)

    weblink = urllib.urlopen(link)
    soup = BeautifulSoup(weblink)

    for i in soup.findAll('img', attrs={'src': re.compile('(?i)(jpg\??)[0-9]*$')}):
        full_url = urlparse.urljoin(link, i['src'])

        if full_url.find("thumbnail"):
            full_url = full_url.replace("thumbnail", "original")
            print "Campaign Original Image: ", full_url
            urllib.urlretrieve(full_url, os.path.join(desktop_folder, 'image%d.jpg' % number))
            number = number+1
            break
        else:
            print "No campaign image found"

def get_links(filename):
    singlelink = tuple(open(filename, 'r'))

    # print singlelink
    for i in singlelink:
        i = i.strip()
        if "http" in i:
            print i
            get_image(i)

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: ./roundupimages.py <filename>\n")
        sys.exit(-1)
    
    filename = sys.argv[1]
    get_links(filename)

if __name__ == '__main__':
    main()
    sys.exit(0)
