# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:19:20 2015

@author: Will
"""

from bs4 import BeautifulSoup
import urllib
import pandas as pd
import re
from datetime import datetime

url="http://finance.yahoo.com/q/h?s=AAPL&t=2015-07-11"
response=urllib.request.urlopen(url)
soup=BeautifulSoup(response,"html.parser")

print(soup.prettify())


# Get Article Hyperlink References and Article Titles
articleHref=[]
articleTitle=[]
for i in soup.find_all(href=re.compile("\/finance\/external\/")):
    articleTitle.append(i.get_text())
    articleHref.append(i.get("href"))               

# Get Article Publishers and Article Dates
publisher=[]
articleDate=[]
for i in soup.find_all(class_="mod yfi_quote_headline withsky"):
    for d in i.find_all("ul"):
        for j in d.find_all("li"):
            for z in j.find_all("a"):
                if z.get("href")[0:31]==str("http://us.rd.yahoo.com/finance/"):
                    for k in j.find_all("cite"):
                        publisher.append(str(k.get_text().split("\xa0")[0]))
                        articleDate.append(str(k.parent.parent.previous_sibling.get_text()))

len("http://us.rd.yahoo.com/finance/")

for i in range(0,len(publisher)):
    if publisher[i][0:2]=="at":
        publisher[i]=publisher[i][3:]
    else:
        publisher[i]=publisher[i]

for i in range(0,len(articleDate)):
    i_replace=str(articleDate[i]).replace(" ","-")
    i_tuple=i_replace.split(",")
    articleDate[i]=str(i_tuple[1]+i_tuple[2])[1:]
    
print(articleDate)


for i in range(0,len(articleDate)):
    articleDate[i]=datetime.strptime(str(articleDate[i]),"%B-%d-%Y")


print(len(articleTitle))            
print(len(articleHref))
print(len(publisher)) 
print(len(articleDate)) 

df = pd.DataFrame({'Title' : articleTitle,
              'Link':articleHref,
              'Publisher': publisher,
              'articleDate':articleDate}
             )


df = df.set_index(df.articleDate)
df.pop('articleDate')
df.info()
df





