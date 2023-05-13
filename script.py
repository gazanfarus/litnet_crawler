#import sys
#from PyQt5 import QApplication
#from PyQt4.QtCore import QUrl
#from PyQt4.QtWebKit import QWebPage
from bs4 import BeautifulSoup
import requests
import itertools
#import urllib.request

#-----------------------Primary run to detect pages and chapters---------
website = 'https://litnet.com/ru/reader/akademiya-smerti-ili-istinnaya-dlya-demona-2-b427431?c=4770785&p=1'
result =requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

#-------Chapter select--------
page_chap = soup.find('div', class_='select_change_arrow')
page = page_chap.select('option[value]')
values = [item.get('value') for item in page]
print(values)

url='https://litnet.com/ru/reader/akademiya-smerti-ili-istinnaya-dlya-demona-2-b427431?c='

url_list=["{}{}&p=".format(url,i) for i in values]

#url_fin=[url_list.append(i) for i in range(1,10)]

#url_fin=["{}{}".format(url_list,i) for i in range(1,10)]

a_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
url_fin = list(map("".join, itertools.product(url_list, a_list)))
print(url_fin)

#------HTML code print------
#print(soup.prettify())

#box = soup.find('div', class_ = 'jsReaderText')
#box = soup.find('div', class_='reader-text font-size-medium')
#jsreader = soup.find('div', class_='jsReaderText')
#textbox = soup.find('p')



#-------------------Print Chapter and Text-------------------
box = soup.find('div', class_='reader-text font-size-medium')
chapter = box.find('h2').get_text()
#print(chapter))
text =[i.text for i in box.find_all('p')]
#print(text)


#----------Junk----------
#transcript = jsreader.find('p').get_text()
#print(transcript)

#test = soup.find('p', style_='text-align:justify;')
#print(test)
