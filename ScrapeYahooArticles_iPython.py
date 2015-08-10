
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
import urllib
import pandas as pd



# In[20]:

url="http://finance.yahoo.com/q/h?s=AAPL&t=2015-07-11"
response=urllib.request.urlopen(url)
soup=BeautifulSoup(response,"html.parser")


# In[21]:

print(soup.prettify())


# In[ ]:




# In[55]:

divHeadlines=[]
divHeadlines=soup.find_all("div", attrs={"class": "mod yfi_quote_headline withsky"})
HrefHeadlines=[]
HrefHeadlines=soup.find_all("a",href=True) 


# In[58]:

for i in HrefHeadlines:
    print(i.get_text())


# In[50]:

Headlines=[]
for div in divHeadlines:
    Headlines.append(div.get_text())

str(Headlines).split("\\xa0")


# In[52]:

Href=[]
for link in HrefHeadlines:
    Href.append(link)

str(HrefHeadlines)


# In[36]:

Href=[]
for link in HrefHeadlines:
    Href.append(link.get_text())


# In[43]:

HrefHeadlines


# In[24]:

HeadlinesTxt=str(Headlines)


# In[27]:

print(HeadlinesTxt)


# In[28]:

print(divHeadlines)


# In[32]:

htmlArticle=div.split("</li>")

print(htmlArticle)

