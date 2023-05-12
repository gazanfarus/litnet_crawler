#import sys
#from PyQt5 import QApplication
#from PyQt4.QtCore import QUrl
#from PyQt4.QtWebKit import QWebPage
from bs4 import BeautifulSoup
import requests
#import urllib.request

website = 'https://litnet.com/ru/reader/akademiya-smerti-ili-istinnaya-dlya-demona-2-b427431?c=4770785&p=1'
result =requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

page_chap = soup.find('div', class_='select_change_arrow')
page = page_chap.select('option[value]')
values = [item.get('value') for item in page]
print(values)


#------HTML code print------
#print(soup.prettify())

#box = soup.find('div', class_ = 'jsReaderText')
box = soup.find('div', class_='reader-text font-size-medium')
#jsreader = soup.find('div', class_='jsReaderText')
#textbox = soup.find('p')



#-------------------Print Chapter and Text-------------------
chapter = box.find('h2').get_text()
#print(chapter))
text = box.find_all('p')
#.get_text()
#print(text)
#transcript = jsreader.find('p').get_text()
#print(transcript)

#test = soup.find('p', style_='text-align:justify;')
#print(test)
