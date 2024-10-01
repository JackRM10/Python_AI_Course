import requests from bs4 import BeautifulSoup

url = "https://learncodeinganywhere.com/"
repsonse = requests.get(url)

soup = BeautifulSoup(repsonse.text, 'html.parser')

title_element = soup.find('title')
if title_element:
    page_title = title_element.text
    print("Page Title:", page_title)
else:
    print("Page title not found.")




