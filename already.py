import sqlite3
import requests
from bs4 import BeautifulSoup

# ? List of Already Read 
already_read = [
"https://www.creepypasta.com/the-door-3/",
"https://www.creepypasta.com/the-8th-shrine/",
"https://www.creepypasta.com/nights-of-fear/", 
"https://www.creepypasta.com/what-are-the-scariest-places-on-google-earth/",
"https://www.creepypasta.com/the-dipping-cup/", 
"https://www.creepypasta.com/a-cold-wind-through-prairie-grass/",
"https://www.creepypasta.com/the-cursed-brass-bell-of-trussville/", 
"https://www.creepypasta.com/dr-greenwichs-flesh-clinic/",
"https://www.creepypasta.com/the-man-in-the-red-tin-wall/", 
"https://www.creepypasta.com/dr-greenwichs-flesh-golem/", 
"https://www.creepypasta.com/all-the-stars-in-the-sky/", 
"https://www.creepypasta.com/the-crimson-queen/", 
"https://www.creepypasta.com/all-you-need-is-a-bucket-of-snails/", 
"https://www.creepypasta.com/the-hive/", 
"https://www.creepypasta.com/the-tained-vase-of-bialowieza-forest/", 
"https://www.creepypasta.com/night-terrors-2/", 
"https://www.creepypasta.com/ive-traveled-to-parallel-universes-the-worlds-ive-seen-are-terrifying-part-3/", 
"https://www.creepypasta.com/halloween-when-the-masks-come-off/", 
"https://www.creepypasta.com/i-hunted-down-a-monster-from-an-alternate-universe/", 
"https://www.creepypasta.com/sympathy-card/",
"https://www.creepypasta.com/the-haunted-toy-car-of-anamosa/", 
"https://www.creepypasta.com/darkness-in-the-rear-view-mirror/", 
"https://www.creepypasta.com/hangman-2/", 
"https://www.creepypasta.com/night-walks/", 
"https://www.creepypasta.com/plot-thirteen/",
"https://www.creepypasta.com/room-for-two/",
"https://www.creepypasta.com/ive-traveled-to-parallel-universes-the-worlds-ive-seen-are-terrifying/", 
"https://www.creepypasta.com/ive-travelled-to-parallel-universes-the-worlds-ive-seen-are-terrifying-part-2/", 
"https://www.creepypasta.com/slenderman/", 
"https://www.creepypasta.com/mr-widemouth/", 
"https://www.creepypasta.com/upon-the-altar/", 
"https://www.creepypasta.com/i-wish-i-had-wings/", 
"https://www.creepypasta.com/gateway-of-the-mind/", 
"https://www.creepypasta.com/the-statue/", 
"https://www.creepypasta.com/ticci-toby/", 
"https://www.creepypasta.com/you-cant-trust-everyone/", 
"https://www.creepypasta.com/dont-let-them-in/", 
"https://www.creepypasta.com/the-terror-in-the-tunnels/", 
"https://www.creepypasta.com/i-dove-to-depths-uncharted-they-should-have-stayed-that-way/", 
"https://www.creepypasta.com/in-the-corner-of-my-eye/", 
"https://www.creepypasta.com/psychosis/", 
"https://www.creepypasta.com/nighty-night/", 
"https://www.creepypasta.com/i-investigate-disturbing-cases-here-are-my-stories-the-woman/", 
"https://www.creepypasta.com/the-face-of-fear/", 
"https://www.creepypasta.com/a-shattered-life/" 
]

#***Tags***
# Pasta Link: Given
# Pasta Header: _self cvplbd
    # Pasta Header: entry-title
# Pasta Time: rt-label rt-prefix
# Pasta Rankin: pt-cv-ctf-value

def Header(list):
    get_header = []
    for url in list:
        result = requests.get(url)
        site = BeautifulSoup(result.text, "html.parser")
        Header = site.find(class_ = "entry-title").text
        get_header.append(Header)
    return get_header
# data = list(zip(Header(already_read),already_read))

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
