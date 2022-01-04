import requests
from bs4 import BeautifulSoup
import smtplib

'''insert page url'''
url = ""

'''search google for "my user agent"'''
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

def check_price():
	page = requests.get(url, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	'''inspect the page to find elements - the title had id so it was like the video tutorial'''
	title = soup.find(id="productTitle").get_text()

	'''The price is find by the class name and the value is parsed to get a float number
	- read the docs, first solution found, probably not the best - worked'''
	find_price = soup.find_all("span", class_="a-offscreen", limit=1)
	parse_price = find_price[0].get_text()
	price = float(parse_price[0:3])

	print(title.strip())
	print(price)

	if price > 150:
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	'''Using the google password method - not working'''
	server.login('[insert username]', '[insert password]')

	subject = 'The price fell down!!!'
	body = 'Check link - [insert url]'

	msg = f"Subject: {subject}\n\n{body}"

	'''insert mails'''
	server.sendmail(
		'[insert from]',
		'[insert to]',
		msg
	)
	print("Email sent!")
	server.quit()

'''add a loop and import time to use sleep() to set a time interval that the code runs'''
check_price()

