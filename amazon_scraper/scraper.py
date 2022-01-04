import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.es/-/pt/dp/B07SPVM6V6/?coliid=I6MIXCMWY5PTQ&colid=2AR107BJQIUMJ&psc=1&ref_=lv_ov_lig_dp_it"

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find_all("span", class_="a-offscreen", limit=1)

parsed_price = price[0].get_text()
final_price = float(parsed_price[0:3])


print(title.strip())
print(parsed_price)
print(final_price)

if final_price < 180:
	print("YES")
else:
	print("HO NO")