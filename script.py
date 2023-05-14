#import sys
#from PyQt5 import QApplication
#from PyQt4.QtCore import QUrl
#from PyQt4.QtWebKit import QWebPage
from bs4 import BeautifulSoup
import requests
import itertools
import time
#import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSessionIdException

options = Options()
options.add_argument("user-data-dir=selenium") 
#options.add_argument('--disable-gpu')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-setuid-sandbox')
#options.add_argument('--disable-dev-shm-usage')
#options.add_argument("--start-maximized")
#options.add_argument("--window-size=1920,1080")
browser = webdriver.Chrome(options=options)
#browser = webdriver.Chrome()

browser.get("https://litnet.com/ru/reader/akademiya-smerti-ili-istinnaya-dlya-demona-2-b427431?c=4770785&p=1")
html = browser.page_source
time.sleep(3)
#print(html)
browser.close()

#driver.close()
#browser.quit()

#-----------------------Primary run to detect pages and chapters---------
#website = 'https://litnet.com/ru/reader/akademiya-smerti-ili-istinnaya-dlya-demona-2-b427431?c=4770785&p=2'
#result = requests.get(website)
#time.sleep(2.5)
#content = result.text
#soup = BeautifulSoup(content, 'lxml')
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())

#-------Chapter select--------
page_chap = soup.find('div', class_='select_change_arrow')
page = page_chap.select('option[value]')
values = [item.get('value') for item in page]
#print(values)

url='https://litnet.com/ru/reader/akademiya-smerti-ili-istinnaya-dlya-demona-2-b427431?c='

url_list=["{}{}&p=".format(url,i) for i in values]

pages = ["1", "2", "3", "4", "5", "6", "7", "8"]
url_fin = list(map("".join, itertools.product(url_list, pages)))
#print(url_fin)

#------HTML code print------
#print(soup.prettify())

#box = soup.find('div', class_ = 'jsReaderText')
#box = soup.find('div', class_='reader-text font-size-medium')
#jsreader = soup.find('div', class_='jsReaderText')
#textbox = soup.find('p')


#---------LOOP---------
#webarray = url_fin
#print(webarray)

for link in url_fin:
	print(link)
	try:
		browser = webdriver.Chrome(options=options)
		browser.get(link)
		time.sleep(3)
		html_loop = browser.page_source
		soup_loop = BeautifulSoup(html_loop, 'lxml')
		browser.close()

#	result_loop = requests.get(link)
#	content_loop = result_loop.text
#	soup_loop = BeautifulSoup(content_loop, 'lxml')


		box = soup_loop.find('div', class_='reader-text font-size-medium')
		try:
			chapter = box.find('h2').get_text()
			print(chapter)
		except:
			print("No chapter found")
		else:
			with open("book.txt") as testfile:
				word = chapter
				inhalt = testfile.read ()
			if word not in inhalt:
				 with open("book.txt", 'a') as testfile:
      					 testfile.write(word+ "\n")
		
		finally:
			text = [i.text for i in box.find_all('p')]
			text_join = ' '.join(text)
			print(text_join)
		
			with open("book.txt") as testfile:
				word1 = text_join
				inhalt = testfile.read ()
			if word1 not in inhalt:
				with open("book.txt", 'a') as testfile:
					testfile.write(word1+ "\n")


			time.sleep(5)
	except InvalidSessionIdException:
		print('FAIL')
