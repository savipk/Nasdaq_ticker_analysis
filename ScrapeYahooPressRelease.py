# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:18:03 2015

@author: Will
"""
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import re
from datetime import datetime

url="http://finance.yahoo.com/q/p?s=AAPL+Press+Releases"
response=urllib.request.urlopen(url)
soup=BeautifulSoup(response,"html.parser")

print(soup.prettify())

pressReleaseHref=[]
pressReleaseTitle=[]
for i in soup.find_all(href=re.compile("\.com\/news\/")):
    pressReleaseTitle.append(i.get_text())
    pressReleaseHref.append(i.get("href")) 

print(pressReleaseHref)
print(pressReleaseTitle)


pressReleasePublisher=[]
pressReleaseDate=[]
for i in soup.find_all(class_="mod yfi_quote_headline withsky"):
    for d in i.find_all("ul"):
        for j in d.find_all("li"):
            for k in j.find_all("cite"):
                pressReleasePublisher.append(str(k.get_text().split("\xa0")[0]))
                pressReleaseDate.append(str(k.parent.parent.previous_sibling.get_text()))                

print(pressReleasePublisher)
print(pressReleaseDate)
                
for i in range(0,len(pressReleasePublisher)):
    for ch1 in ["("]:
        if ch1 in str(pressReleasePublisher[i]):
            pressReleasePublisher[i]=str(pressReleasePublisher[i]).replace(ch1,"")

for i in range(0,len(pressReleaseDate)):
    i_replace=str(pressReleaseDate[i]).replace(" ","-")
    i_tuple=i_replace.split(",")
    pressReleaseDate[i]=str(i_tuple[1]+i_tuple[2])[1:]

for i in range(0,len(pressReleaseDate)):
    pressReleaseDate[i]=datetime.strptime(str(pressReleaseDate[i]),"%B-%d-%Y")

print(len(pressReleaseTitle))            
print(len(pressReleaseHref))
print(len(pressReleasePublisher)) 
print(len(pressReleaseDate))

df = pd.DataFrame({'Title' : pressReleaseTitle,
              'Link':pressReleaseHref,
              'Publisher': pressReleasePublisher,
              'pressReleaseDate':pressReleaseDate}
             )

df = df.set_index(df.pressReleaseDate)
df.pop('pressReleaseDate')
df.info()
df



