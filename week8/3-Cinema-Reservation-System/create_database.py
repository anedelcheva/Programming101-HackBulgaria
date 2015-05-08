create_table_movies = '''
CREATE TABLE IF NOT EXISITS Movies(
id INTEGER PRIMARY KEY,
name TEXT,
rating REAL
)'''

create_table_projections = '''
id INTEGER PRIMARY KEY,
FOREIGN KEY(movie_id) REFERENCES Movies(id)

'''
