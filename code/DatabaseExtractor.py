import sqlite3


def read_data(table, row):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT " + row + " FROM " + table)

    return cursor.fetchall()


def read_id(table, row, id):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT " + row + " FROM " + table + " WHERE player_api_id= " + id + " ")

    return cursor.fetchall()

#    file = open("database", "w+")
#   file.write(str(row))
#  file.close()
# db.close()

# inputs: list of player ID's, needed player stat,
# Read in the data of the match and of the players
# player_ID needs to be an list of player_ID's, for example by calling "read_data("Match", "home_player_1")[:1000]"
# needed_stat is the player stat that you want to extract
# standard_value is the standard value that will be used if the ID equals None
def stats_from_id(player_ID, needed_stat, standard_value):
    api_id = read_data("Player_Attributes", "player_api_id, " + needed_stat)

    # Make sure the overall rating of every player is available, if the player ID is NONE, a custom value is parsed in.
    p1_rating = []
    #for every player 1 of a match
    for item in player_ID:
        # Parse in some value if None, else parse in the player strength
        if item[0] is None:
            p1_rating.append([standard_value])
        else:
            for i in range(len(api_id)):

                if item[0] == api_id[i][0]:
                    #print("found!")
                    p1_rating.append([api_id[i][1]])

                    break
    return p1_rating



