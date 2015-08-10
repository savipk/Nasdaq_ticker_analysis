from bs4 import BeautifulSoup
import urllib
import pandas as pd
url="http://finance.yahoo.com/q/ud?s=AAPL"
response=urllib.request.urlopen(url)
soup=BeautifulSoup(response,"html.parser")
print(soup.prettify())
AnalystDec=soup.find_all("td", attrs={"class": "yfnc_tabledata1"})
AnalystDec=str(AnalystDec)
AnalystDec.split(",")
AnalystDec=[]
AnalystDec=soup.find_all("td", "yfnc_tabledata1")
text = []
step = 0
row = []
for i in AnalystDec:
       row.append(i.get_text())
       if step > 3:
               text.append(row)
               step = 0
               row = []
       else:
               step = step + 1
print(text)
headers=['Date','Research Firm', 'Action', 'From', 'To']
df = pd.DataFrame(text,columns=headers)
df.index=df.Date
df.loc['5-Aug-15']




