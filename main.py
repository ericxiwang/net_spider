__author__ = 'ericwang'

import urllib2

import re
from bs4 import BeautifulSoup

target_url = "http://www.timedrugs.com/cn/index.aspx"
open_url = urllib2.urlopen(target_url)
text_content = open_url.read()

soup = BeautifulSoup(text_content)

aa = soup.find_all("a",class_="zth12")
for i in range(len(aa)):
    print aa[i]

bb = soup.find_all("div",style="text-decoration: line-through;")
for z in range(len(bb)):
    print bb[z]

cc = soup.find_all("td",class_="text_07")
for y in range(len(cc)):
    print cc[y]
