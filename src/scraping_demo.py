import requests
from bs4 import BeautifulSoup


url = "https://example.com"

response = requests.get(url, timeout=30)

print("Status Code:", response.status_code)

html = response.text

soup = BeautifulSoup(html, "html.parser")

print()
print("Page Title:")
print(soup.title.text)

print()
print("Main Heading:")
print(soup.find("h1").text)