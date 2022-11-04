import sqlite3
import random
toRead = r"/home/davidcok/Coding/Python/creepy_pasta_project/toRead.db"
alread = r"/home/davidcok/Coding/Python/creepy_pasta_project/alread.db"
connect = sqlite3.connect(toRead)
connect_alread = sqlite3.connect(alread)
connect.execute("ATTACH ? AS Purge_Copies", [alread])
# connect = sqlite3.connect(alread)
# ? Test Output:
# cursor = connect.cursor()
# for row in cursor.execute("SELECT Title FROM toRead"):
    # print(row)
purge = connect.execute("SELECT * FROM toRead WHERE Title NOT IN(SELECT Title FROM alread)").fetchall()
# for i in purge:
    # print(i)
def generate_random(purge):
    reading = random.choice(purge)
    return reading
def rating_range():
    print()
def time_range():
    print()

print(generate_random(purge))