import sqlite3


def read_data(table, row):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT " + row + " FROM " + table)

    return cursor.fetchall()


#    file = open("database", "w+")
#   file.write(str(row))
#  file.close()
# db.close()


