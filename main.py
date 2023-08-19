import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for quote, author in zip(quotes, authors):
    print("Quote:", quote.get_text())
    print("Author:", author.get_text())
    print()
