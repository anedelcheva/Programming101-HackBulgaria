import sqlite3


database = sqlite3.connect('students_and_courses.db')
database.row_factory = sqlite3.Row
cursor = database.cursor()


def list_students_name_account():
    cursor.execute('SELECT student_name, github_account FROM Students')
    all_students = cursor.fetchall()
    return all_students


def list_all_courses():
    cursor.execute('SELECT course_name FROM Courses')
    all_courses = cursor.fetchall()
    return all_courses


def get_student_id(student_name):
    cursor.execute('SELECT student_id FROM Students WHERE student_name=?', (student_name,))
    stud_id = cursor.fetchone()
    return stud_id[0]


def get_student_name(student_id):
    cursor.execute('SELECT student_name FROM Students WHERE student_id=?', (student_id,))
    stud_name = cursor.fetchone()
    return stud_name[0]


def get_students_ids():
    cursor.execute('SELECT student_id FROM Students')
    ids = cursor.fetchall()
    students_ids = []
    for stud_id in ids:
        students_ids.append(stud_id['student_id'])
    return students_ids


def get_course_ids_of_student(student_id):
    cursor.execute('''SELECT course_id FROM Course_assignments
                    WHERE student_id=?''', (student_id,))
    course_ids = cursor.fetchall()
    courses = []
    for row in course_ids:
        courses.append(row['course_id'])
    return courses


def get_course_name(course_id):
    cursor.execute('SELECT course_name FROM Courses WHERE course_id=?', (course_id,))
    name = cursor.fetchone()
    return name[0]


def list_courses_of_student(student_id):
    course_ids = get_course_ids_of_student(student_id)
    courses = set()
    for course_id in course_ids:
        courses.add(get_course_name(course_id))
    return courses


def student_courses_dict(student_id):
    student_name = get_student_name(student_id)
    student_courses = {}
    courses_of_student = list_courses_of_student(student_id)
    student_courses[student_name] = courses_of_student
    return student_courses


def get_students_names():
    cursor.execute('''SELECT student_name FROM Students''')
    name_objs = cursor.fetchall()
    students_names = []
    for index in range(len(name_objs)):
        students_names.append(name_objs[index]['student_name'])
    return students_names


def students_and_courses():
    students_courses = []
    students_ids = get_students_ids()
    for stud_id in students_ids:
        print (stud_id, list_courses_of_student(stud_id))
    for stud_id in students_ids:
        students_courses.append(student_courses_dict(stud_id))
    return students_courses


def students_most_attending():
    students_ids = get_students_ids()
    most_attending = set()
    for stud_id in students_ids:
        courses_of_student = list_courses_of_student(stud_id)
        if (len(courses_of_student) >= 3):
            student_name = get_student_name(stud_id)
            most_attending.add(student_name)
    return most_attending
