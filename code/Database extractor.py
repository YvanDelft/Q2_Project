import sqlite3

db = sqlite3.connect('database.sqlite')
cursor = db.cursor()
cursor.execute("""SELECT season, stage, date FROM match """)

rows = cursor.fetchall()

#for row in rows:
#    print(row)
print(rows)


