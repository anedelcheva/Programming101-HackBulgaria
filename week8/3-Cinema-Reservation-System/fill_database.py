import sqlite3
from settings import DB_NAME

# we connect to the database with name DB_NAME
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


# Filling in table Movies
name1 = "The Hunger Games: Catching Fire"
rating1 = 7.9
name2 = "Wreck-It Ralph"
rating2 = 7.8
name3 = "Her"
rating3 = 8.3
cursor.execute('INSERT INTO Movies(name, rating) VALUES(?, ?)', (name1, rating1))
cursor.execute('INSERT INTO Movies(name, rating) VALUES (?, ?)', (name2, rating2))
cursor.execute('INSERT INTO Movies(name, rating) VALUES (?, ?)', (name3, rating3))


# Filling in table Projections
movie_id1 = 1
type1 = '3D'
date1 = '2014-04-01'
time1 = '19:10'
movie_id2 = 1
type2 = '2D'
date2 = '2014-04-01'
time2 = '19:00'
movie_id3 = 1
type3 = '4DX'
date3 = '2014-04-02'
time3 = '21:00'
movie_id4 = 3
type4 = '2D'
date4 = '2014-04-05'
time4 = '20:20'
movie_id5 = 2
type5 = '3D'
date5 = '2014-04-02'
time5 = '22:00'
movie_id6 = 2
type6 = '2D'
date6 = '2014-04-02'
time6 = '19:30'

cursor.execute('''INSERT INTO Projections(movie_id, type, date, time)
                VALUES (?, ?, ?, ?)''', (movie_id1, type1, date1, time1))
cursor.execute('''INSERT INTO Projections(movie_id, type, date, time)
                VALUES (?, ?, ?, ?)''', (movie_id2, type2, date2, time2))
cursor.execute('''INSERT INTO Projections(movie_id, type, date, time)
                VALUES (?, ?, ?, ?)''', (movie_id3, type3, date3, time3))
cursor.execute('''INSERT INTO Projections(movie_id, type, date, time)
                VALUES(?, ?, ?, ?)''', (movie_id4, type4, date4, time4))
cursor.execute('''INSERT INTO Projections(movie_id, type, date, time)
                VALUES(?, ?, ?, ?)''', (movie_id5, type5, date5, time5))
cursor.execute('''INSERT INTO Projections(movie_id, type, date, time)
                VALUES (?, ?, ?, ?)''', (movie_id6, type6, date6, time6))


# Filling in table Reservations
username1 = 'RadoRado'
projection_id1 = 1
row1 = 2
col1 = 1
username2 = 'RadoRado'
projection_id2 = 1
row2 = 3
col2 = 5
username3 = 'RadoRado'
projection_id3 = 1
row3 = 7
col3 = 8
username4 = 'Ivo'
projection_id4 = 3
row4 = 1
col4 = 1
username5 = 'Ivo'
projection_id5 = 3
row5 = 1
col5 = 2
username6 = 'Mysterious'
projection_id6 = 5
row6 = 2
col6 = 3
username7 = 'Mysterious'
projection_id7 = 5
row7 = 2
col7 = 4

cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                VALUES(?, ?, ?, ?)''', (username1, projection_id1, row1, col1))
cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                VALUES(?, ?, ?, ?)''', (username2, projection_id2, row2, col2))
cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                VALUES(?, ?, ?, ?)''', (username3, projection_id3, row3, col3))
cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                VALUES(?, ?, ?, ?)''', (username4, projection_id4, row4, col4))
cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                VALUES(?, ?, ?, ?)''', (username5, projection_id5, row5, col5))
cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                VALUES(?, ?, ?, ?)''', (username6, projection_id6, row6, col6))
cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                VALUES(?, ?, ?, ?)''', (username7, projection_id7, row7, col7))

conn.commit()
