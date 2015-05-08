DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Projections;
DROP TABLE IF EXISTS Reservations;

CREATE TABLE Movies(
id INTEGER PRIMARY KEY,
name TEXT,
rating REAL
);

CREATE TABLE Projections(
id INTEGER PRIMARY KEY,
movie_id INTEGER,
type TEXT,
date TEXT,
time TEXT,
FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

CREATE TABLE Reservations(
id INTEGER PRIMARY KEY,
username TEXT,
projection_id INTEGER,
row INTEGER,
col INTEGER,
FOREIGN KEY (projection_id) REFERENCES Projections(id)
);
