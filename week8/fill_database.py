import requests
import sqlite3
from write_and_load_files import writeToFile
from write_and_load_files import loadFromFile


hackbg_api = requests.get('https://hackbulgaria.com/api/students/').text
writeToFile('students.txt', hackbg_api)
students_list = loadFromFile('students.txt')
db = sqlite3.connect('students_and_courses.db')
cursor = db.cursor()


def get_student_name(index):
    return students_list[index]['name']


def get_github_account(index):
    return students_list[index]['github']


def get_available(index):
    available = students_list[index]['available']
    if available == False:
        return 0
    else:
        return 1


def put_students_to_db():
    for index in range(len(students_list)):
        name = get_student_name(index)
        github_account = get_github_account(index)
        available = get_available(index)
        cursor.execute('''INSERT INTO Students(student_name, github_account, available)
            VALUES(?, ?, ?)''', (name, github_account, available))
    db.commit()


put_students_to_db()


# returns a list of students' courses
def get_course_names(index):
    return students_list[index]['courses']


def put_courses_to_set():
    courses = set()
    for index in range(len(students_list)):
        courses_list = get_course_names(index)
        for course in courses_list:
            courses.add(course["name"])
    return courses


def put_courses_to_db():
    courses_set = put_courses_to_set()
    for course in courses_set:
        cursor.execute('''INSERT INTO Courses(course_name) VALUES (?)''', (course,))
    db.commit()


def get_courses(index):
    courses = students_list[index]['courses']
    courses_list = []
    for course in courses:
        courses_list.append(course['name'])
    return courses_list


def get_group(index):
    courses = students_list[index]['courses']
    groups = []
    for course in courses:
        groups.append(course['group'])
    return groups


def get_courses_and_groups(index):
    courses = students_list[index]['courses']
    courses_groups = {}
    for course in courses:
        group_number = course['group']
        course_name = course['name']
        courses_groups[course_name] = group_number
    return courses_groups


put_courses_to_db()


# filling in the junction table
def fill_junction_table():
    for index in range(len(students_list)):
        name = get_student_name(index)
        cursor.execute('''SELECT student_id FROM Students
                        WHERE student_name=?''', (name,))
        stud_id = cursor.fetchone()
        courses_groups = get_courses_and_groups(index)
        for course in courses_groups:
            group_number = courses_groups[course]
            cursor.execute('''SELECT course_id FROM Courses
                            WHERE course_name=?''', (course,))
            course_id = cursor.fetchone()
            cursor.execute('''INSERT INTO Course_assignments
                (course_id, student_id, group_number) VALUES(?, ?, ?)''',
                (course_id[0], stud_id[0], group_number))
    db.commit()


fill_junction_table()
