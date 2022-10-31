import sqlite3

#Creates an IMDB rating collection table
conn = sqlite3.connect('movieInfoDB.db')
cursor = conn.cursor()    
# cursor.execute("DROP TABLE IF EXISTS IMDBmovieInfo;")
cursor.execute('''CREATE TABLE IF NOT EXISTS IMDBmovieInfo(
                            movie_name TEXT PRIMARY KEY,
                            year INT, 
                            actors TEXT,
                            rating INT);''')
#=================
#ensure rating is always >=0 and <=10
#I am removing description TEXT column for now
#We shall add it when everything else works fine
#================
cursor.close()  
                   