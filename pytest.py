#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re
from bs4 import BeautifulSoup

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getMovie(html):
    soup = BeautifulSoup(''.join(html))
    trs = soup.find_all("tr")
    for tr in trs:
        types = tr.find_all("td",{'class':'hall-type'})
        for t in types:
            print t.string
        prices = tr.find_all("em",{'class':'now'})
        for p in prices:
            print p.string
        

    body = re.compile(r'<tbody>([\s\S]+)</tbody>')
    movieDiv = re.compile(r'<tr([\s\S]+)</tr>')
    startTime = re.compile(r'<em class="bold">(.*)</em>')
    price = re.compile(r'<em class="now">(.*)</em>')
    body = re.findall(body,html)[0]

    movieList = body.split("</tr>")
    


html = getHtml("http://dianying.taobao.com/showDetailSchedule.htm?showId=27241&ts=1432458581390&n_s=new")
getMovie(html)