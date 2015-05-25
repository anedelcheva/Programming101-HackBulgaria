import sqlite3
from settings import DB_NAME


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
cursor = db.cursor()
SPOTS = 100

SEATS = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
]


COMMANDS = ['show_movies', 'show_movie_projections', 'make_reservation', 'help']


def show_movies():
    query = 'SELECT * FROM Movies ORDER BY rating'
    print("Current movies:")
    cursor.execute(query)
    movies = cursor.fetchall()
    for movie in movies:
        print ('[{}] - {} ({})'.format(movie['id'],
                                       movie['name'],
                                       movie['rating']))


def show_movie_projections(movie_id):
    movies_and_their_projections = '''
    SELECT Movies.name, Projections.id, Projections.date,
    Projections.time, Projections.type
    FROM Projections
    JOIN Movies
    ON Projections.movie_id = Movies.id
    WHERE Projections.movie_id = ?
    ORDER BY Projections.date
    '''
    cursor.execute(movies_and_their_projections, (movie_id,))
    projections = cursor.fetchall()
    number_of_reservations_for_projection = '''
    SELECT COUNT(*)
    FROM Projections
    JOIN Movies
    ON Projections.movie_id = Movies.id
    JOIN Reservations
    ON Reservations.projection_id = Projections.id
    WHERE Movies.id = ? AND Projections.id = ?
    ORDER BY Projections.date'''
    if projections == []:
        print ("There is no movie with this id!")
    else:
        print ("Projections for movie '{}':".format(projections[0]['name']))
        for projection in projections:
            cursor.execute(number_of_reservations_for_projection,
                          (movie_id, projection['id']))
            reserved_spots = cursor.fetchone()[0]
            print ('[{}] - {} {} ({}) - {} spots available'
                .format(projection['id'],
                        projection['date'],
                        projection['time'],
                        projection['type'],
                        SPOTS - reserved_spots))


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
    print ("Projections for movie '{}' on date {}:"
            .format(movies[0]['name'], movie_date))
    for movie in movies:
        if movie['date'] == movie_date:
            print ('[{}] - {} ({})'.format(movie['id'],
                                           movie['time'],
                                           movie['type']))


def reserve_seat(name, projection_id, row, col):
    name_seat = '''
    INSERT INTO Reservations(username, projection_id, row, col)
    VALUES(?, ?, ?, ?)'''
    cursor.execute(name_seat, (name, projection_id, row, col))
    db.commit()


def reserved_seats(projection_id):
    query = '''SELECT row, col
               FROM Reservations
               WHERE projection_id = ?'''
    cursor.execute(query, (projection_id,))
    res_seats = cursor.fetchall()
    seats = []
    for seat in res_seats:
        seats.append((seat['row'], seat['col']))
    return seats


def matrix_to_map(seats):
    seats_map = ''
    seats_map += '  '
    for number in range(1, 11):
        seats_map += ' '
        seats_map += str(number)
    counter = 1
    for seat in seats:
        seats_map += '\n'
        seats_map += str(counter)
        if counter < 10:
            seats_map += '  '
        else:
            seats_map += ' '
        counter += 1
        current_row = ' '.join(seat)
        seats_map += current_row
    print (seats_map)


def projections_ids():
    query = 'SELECT id FROM Projections'
    cursor.execute(query)
    projections = cursor.fetchall()
    ids = []
    for projection in projections:
        ids.append(projection['id'])
    return ids


def take_available_seats(projection_id):
    if projection_id not in projections_ids():
        print ('No such projection!')
        return
    seats = reserved_seats(projection_id)
    for seat in seats:
        SEATS[seat[0] - 1][seat[1] - 1] = 'X'
    return matrix_to_map(SEATS)


def available_seats_for(projection_id):
    print("Available seats (marked with a dot):")
    return take_available_seats(projection_id)


def choose_seat(projection_id, row, col):
    if (row, col) in reserved_seats(projection_id):
        print ("This seat is already taken!")
        return False
    elif row not in range(1, 11) or col not in range(1, 11):
        print ("No such seat!")
        return False
    return True


def number_of_seats_available_for(projection_id):
    if projection_id not in projections_ids():
        print ("No such projection!")
        return
    query = 'SELECT COUNT(*) FROM Reservations WHERE projection_id = ?'
    cursor.execute(query, (projection_id,))
    return SPOTS - cursor.fetchone()[0]


def movie_name_and_rating(movie_id):
    query = 'SELECT name, rating FROM Movies WHERE id = ?'
    cursor.execute(query, (movie_id,))
    movie = cursor.fetchone()
    print ("Movie: {} ({})".format(movie['name'], str(movie['rating'])))


def movie_date_time_type(movie_id, projection_id):
    query = '''SELECT date, time, type
               FROM Projections
               WHERE movie_id = ?
               AND id = ?'''
    cursor.execute(query, (movie_id, projection_id))
    movie = cursor.fetchone()
    print ('Date and Time: {} {} ({})'
            .format(movie['date'], movie['time'], movie['type']))


def finalize():
    print ("Thanks.")


def remove_brackets_from_tuple(seat):
    seat = seat.strip('() ')
    seat = seat.split(',')
    seat[0] = int(seat[0])
    seat[1] = int(seat[1])
    return tuple(seat)


def does_movie_have_this_projection_id(movie_id, projection_id):
    query = 'SELECT id FROM Projections WHERE id = ? AND movie_id = ?'
    cursor.execute(query, (projection_id, movie_id))
    projections = cursor.fetchone()
    if projections is None:
        print ("There is no such projection for this movie.")
        return False
    return True


def make_reservation():
    while True:
        step1 = "Step 1 (User): Choose "
        name = input(step1 + "name> ")
        num_tickets = input(step1 + "number of tickets> ")
        show_movies()
        step2 = "Step 2 (Movie): Choose a movie> "
        movie_id = input(step2)
        show_movie_projections(int(movie_id))
        step3 = "Step 3 (Projection): Choose a projection> "
        projection_id = input(step3)
        if not does_movie_have_this_projection_id(int(movie_id), int(projection_id)):
            continue
        available_seats_for(int(projection_id))
        num_available_seats = number_of_seats_available_for(int(projection_id))
        if num_available_seats < int(num_tickets):
            print ("You cannot reserve {} seats. Available seats: {}."
                    .format(num_tickets, num_available_seats))
            continue
        step4 = "Step 4 (Seats): Choose seat"
        counter = 0
        seats = []
        while counter != int(num_tickets):
            seat = input('{} {}> '.format(step4, str(counter + 1)))
            seat = remove_brackets_from_tuple(seat)
            row = seat[0]
            col = seat[1]
            if choose_seat(int(projection_id), row, col):
                seats.append(seat)
                reserve_seat(name, int(projection_id), row, col)
                counter += 1
        for i in range(len(seats)):
            seats[i] = str(seats[i])
        seats = ', '.join(seats)
        print ("This is your reservation:")
        movie_name_and_rating(int(movie_id))
        movie_date_time_type(int(movie_id), int(projection_id))
        print ('Seats: {}'.format(seats))
        final = input("Step 5 (Confirm - type 'finalize') > ")
        if final == 'finalize':
            finalize()
            break


def list_commands():
    print ('Type in one of the following commands:')
    for command in COMMANDS:
        print (command)


def parse_command(command):
    return tuple(command.split(" "))


def main():
    while True:
        command = input('> ')
        command = parse_command(command)
        if command[0] not in COMMANDS:
            print ('No such command!')
        elif command[0] == 'show_movies':
            show_movies()
        elif command[0] == 'show_movie_projections':
            if len(command) == 1:
                print("No given id!")
            elif len(command) == 2:
                show_movie_projections(int(command[1]))
            elif len(command) == 3:
                show_movie_projections_with_date(int(command[1]), command[2])
        elif command[0] == 'make_reservation':
            make_reservation()
        elif command[0] == 'help':
            list_commands()


if __name__ == '__main__':
    main()
