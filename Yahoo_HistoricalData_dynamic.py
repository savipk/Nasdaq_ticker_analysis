# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 01:54:37 2015

@author: Will
"""

from bs4 import BeautifulSoup
import urllib
import re
import numpy as np
import pandas as pd
import datetime

# Methods
def string_date_get_month(strDate):
    monthDict={'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    abbrv=str(strDate[0:3]).strip()
    return(monthDict[abbrv])

def string_date_get_day(strDate):
    if int(str(strDate[4:6]).strip()) <10:
        return(str("0"+strDate[5:6]))
    else:
        return(str(strDate[4:6]))
        
def string_date_get_year(strDate):
    return(str(strDate[8:12]))

def string_conversion_datetime(strDate):
    yr=string_date_get_year(strDate)
    mnth=string_date_get_month(strDate)
    dy=string_date_get_day(strDate)
    outDate=datetime.date(yr,mnth,dy)
    return(outDate)


# Example Site uses AAPL
# Uses Dates:
# Start:    07/27/15
# End:      07/31/15

# Date Variables


page = urllib.request.urlopen("http://finance.yahoo.com/q/hp?s=AAPL&a=06&b=27&c=2015&d=07&e=2&f=2015&g=d")

soup= BeautifulSoup(page,"html.parser")

tablePriceData=[]
tablePriceData = soup.find_all("td", "yfnc_tabledata1")

tablePriceHeaders=[]
tablePriceHeaders = soup.find_all("th", "yfnc_tablehead1")

tableHeader=[]
tableData=[]


for header in tablePriceHeaders:
    tableHeader.append(header.get_text())
tableHeader[6]=tableHeader[6][:9]

for priceData in tablePriceData[:-1]:
    tableData.append(priceData.get_text())

headers=[]
headers= [ tableHeader[i] for i in range(7) ]



days = int(len(tableData)/7)

myArray=[[0 for j in range(7)] for i in range(days)]

#k=0
#for i in range(1):
#    for j in range(7):
#        myArray[i][j]=tableData[k]
#        k=k+1

#myArray[0]=[ tableHeader[i] for i in range(7) ]

k=0
for i in range(days):
    for j in range(7):
        myArray[i][j]=tableData[k]
        k=k+1
        
myArray
numArray=np.array(myArray)











# Create DataFrame
#df = pd.DataFrame(numArray,columns=headers)

# Change Time String to Datetime.Timestamp




