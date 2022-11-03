import sqlite3
import requests
from bs4 import BeautifulSoup

element_dict = {
    'time':'',
    'header':'_self cvplbd',
    'ranking':''
}
get_header = []
get_link = []

def get_elements(key,value,site):
    for header in site.find(class_="pt-cv-title"):
        get_header.append(header)

for i in range(1,6):
    url = "https://www.creepypasta.com/?_page=" + str(i)
    result = requests.get(url)
    site = BeautifulSoup(result.text, "html.parser")
    for key, value in element_dict.items():
        get_elements(key,value,site)

print(get_header)
print()
# print(get_link)

# url = "https://www.creepypasta.com/" 


