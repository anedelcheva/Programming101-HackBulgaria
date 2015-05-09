import sqlite3
from settings import DB_NAME


conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
SPOTS = 100


def show_movies():
    cursor.execute('SELECT * FROM Movies ORDER BY rating')
    movies = cursor.fetchall()
    print ('Current movies:')
    for movie in movies:
        print ('[{}] - {} ({})'.format(movie['id'], movie['name'], movie['rating']))


def choose_projection(projection_id):
    cursor.execute('''
    SELECT Projections.id, Movies.name, Projections.type,
    Projections.date, Projections.time
    FROM Projections
    JOIN Movies
    ON Movies.id = Projections.movie_id
    WHERE Projections.id=?''', (projection_id,))
    return cursor.fetchone()


def projections():
    cursor.execute('SELECT Projections.id FROM Projections')
    all_projections = set()
    for proj in cursor.fetchall():
        all_projections.add(proj['id'])
    return all_projections


def projections_number_reservations():
    cursor.execute('''
    SELECT Projections.id, COUNT(Projections.id) AS number
    FROM Projections
    JOIN Reservations
    ON Projections.id = Reservations.projection_id
    GROUP BY Projections.id''')
    projections_reserved = set()
    for proj in cursor.fetchall():
        projections_reserved.add(proj['id'])
    return projections_reserved


def spots_number():
    print ("Total number of spots available for each projection: ")

    cursor.execute('''
    SELECT Projections.id, Movies.name, Projections.type,
    Projections.date, Projections.time, COUNT(Projections.id) AS number
    FROM Projections
    JOIN Reservations
    JOIN Movies
    ON Projections.id = Reservations.projection_id AND Projections.movie_id = Movies.id
    GROUP BY Projections.id''')

    for proj in cursor.fetchall():
        spots = SPOTS - proj['number']
        id = proj['id']
        name = proj['name']
        type = proj['type']
        date = proj['date']
        time = proj['time']
        print ('[{}] - {} ({}) {} {}--->Spots: {}'.format(id, name, type, date, time, spots))

    all_projections = projections()
    projections_reserved = projections_number_reservations()

    for proj in all_projections:
        if proj not in projections_reserved:
            projection = choose_projection(proj)
            id = projection['id']
            name = projection['name']
            type1 = projection['type']
            date = projection['date']
            time = projection['time']
            print('[{}] - {} ({}) {} {}--->Spots: {}'.format(id, name, type1, date, time, SPOTS))


def movie_projections(movie_id):
    cursor.execute('''
    SELECT Movies.name, Projections.id, Projections.date,
    Projections.time, Projections.type
    FROM Projections
    JOIN Movies
    ON Movies.id = Projections.movie_id
    WHERE Projections.movie_id = ?
    ORDER BY Projections.date''', (movie_id,))
    return cursor.fetchall()


def show_movie_projections_with_date(movie_id, movie_date):
    movies = movie_projections(movie_id)
    print ("Projections for movie '" + movies[0]['name'] + "' on date " + movie_date + ':')
    for movie in movies:
        if movie['date'] == movie_date:
            print ('[{}] - {} ({})'.format(movie['id'], movie['time'], movie['type']))
    spots_number()


def show_movie_projections_without_date(movie_id):
    movies = movie_projections(movie_id)
    print ("Projections for movie '" + movies[0]['name'] + "':")
    for movie in movies:
        id = movie['id']
        date = movie['date']
        time = movie['time']
        type = movie['type']
        print ('[{}] - {} {} ({})'.format(id, date, time, type))

    spots_number()


def parse_command(command):
    return tuple(command.split(" "))


def read_command():
    while True:
        command = input('> ')
        command = parse_command(command)
        if command[0] == 'show_movies':
            show_movies()
        elif command[0] == 'show_movie_projections':
            if len(command) == 2:
                show_movie_projections_without_date(int(command[1]))
            elif len(command) == 3:
                show_movie_projections_with_date(int(command[1]), command[2])
            elif len(command) == 1:
                print('No given id!')


def main():
    read_command()


if __name__ == '__main__':
    main()


# show_movie_projections_without_date(1)
# spots_number()
# print (choose_projection(4))
