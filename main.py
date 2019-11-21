#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
html = requests.get('www.pixiv.com')
print (html.status_code)
soup = BeautifulSoup(html.text)
print (soup.prettify())
