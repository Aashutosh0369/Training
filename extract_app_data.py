import requests
from bs4 import BeautifulSoup

url = 'https://apps.odoo.com/apps/modules/17.0/om_account_accountant/'

response = requests.get(url)
html_Content = response.content

soup = BeautifulSoup(html_Content,'lxml')

app = soup.find('div',class_='loempia_app_title')
app_name = app.find('h1', class_='mt0 mb0').text.strip()
print("App Name :",app_name)
author = app.find_all('a')
for i in author:
	a_name = i.find('span',itemprop='name')
	if a_name is None:
		continue
	print("Auther :",a_name.text)
	
rating = soup.find('span',class_='loempia_rating_stars').text.strip()
print(f"Rating is {rating}")	

total_download = soup.find('span',title='Downloads').text.strip()
print(f"Total download is {total_download}")

description = soup.find('div',class_='document').text
print("App details are as follows")
print(description)

other_details = soup.find('div' , class_='oe_styling_v8').text.strip()

img_links = [img['src'] for img in soup.find_all('img')]

text_img_map = dict(zip(other_details.split('\n\n'),img_links))

print('Other details with image link as follows')
for details,img_link in text_img_map.items():
	print(details,img_link)
	print()
