import sqlite3


create_table_students = '''
CREATE TABLE IF NOT EXISTS Students(
student_id INTEGER PRIMARY KEY,
student_name TEXT,
github_account TEXT,
available INTEGER
)'''

create_table_courses = '''
CREATE TABLE IF NOT EXISTS Courses(
course_id INTEGER PRIMARY KEY,
course_name TEXT UNIQUE
)'''

create_table_students_to_courses = '''
CREATE TABLE IF NOT EXISTS Course_assignments(
assignment_id INTEGER PRIMARY KEY,
course_id INTEGER,
student_id INTEGER,
group_number INTEGER,
FOREIGN KEY(student_id) REFERENCES Students(student_id),
FOREIGN KEY(course_id) REFERENCES Courses(course_id)
)'''

conn = sqlite3.connect('students_and_courses.db')
cursor = conn.cursor()
cursor.execute(create_table_students)
cursor.execute(create_table_courses)
cursor.execute(create_table_students_to_courses)
