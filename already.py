import sqlite3
import requests
from bs4 import BeautifulSoup

# ? If you enjoy reading CreepyPastas & have a catalog, past your list of finished
# pastas into 'already_read'
already_read = [...]

def Header(list):
    get_header = []
    for url in list:
        result = requests.get(url)
        site = BeautifulSoup(result.text, "html.parser")
        Header = site.find(class_ = "entry-title").text
        get_header.append(Header)
    return get_header
data = list(zip(Header(already_read),already_read))

# ? Establishes connection with 'Already Read' Database:
connect = sqlite3.connect("alread.db")
cursor = connect.cursor()

# cursor.execute("CREATE TABLE alread (Title text, Link text)")
# cursor.executemany("INSERT INTO alread values (?,?)",data)

# for i in cursor.execute("SELECT * FROM alread"):
#     print(i)
connect.commit()

def manual_input():
    num_input = input("How many readings do you want to input? ")
    i = 0
    # manual_input = []
    lst = []
    while(i != int(num_input)):
        i+=1
        link = input("Paste reading link: ")
        lst.append(link)
    manual_data = list(zip(Header(lst),lst))
    # manual_input.append(manual_data)
    return manual_data
header_links = manual_input()
# print(header_links)
cursor.executemany("INSERT INTO alread values (?,?)",header_links)
for i in cursor.execute("SELECT * FROM alread"):
    print(i)
