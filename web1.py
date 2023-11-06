import requests
URL = "https://www.w3schools.com/"
page = requests.get(URL)
print(page.text)