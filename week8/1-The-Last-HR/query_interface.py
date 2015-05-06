from the_last_hr import (list_students_name_account, list_all_courses,
    students_and_courses, students_most_attending)


commands = {'list_students', 'list_courses', 'students_and_their_courses',
'students_most_attending', 'help'}


def list_students():
    all_students = list_students_name_account()
    for row in all_students:
        print ('{} - {}'. format(row['student_name'], row['github_account']))


def list_courses():
    all_courses = list_all_courses()
    for row in all_courses:
        print (row['course_name'])


def list_students_and_their_courses():
    students_courses = students_and_courses()
    for student_course in students_courses:
        for student in student_course:
            print ('->' + student + ':')
            for course in student_course[student]:
                print ('- {}'.format(course))


def list_students_most_attending():
    most_attending = students_most_attending()
    for student in most_attending:
        print (student)


def list_commands():
    print ('You can type in the following commands:')
    for command in commands:
        print (command)


def is_command(command):
    return command in commands


def read_command():
    while True:
        command = input('command>')
        if not is_command(command):
            print ('No such command')
        if command == 'list_students':
            list_students()
        elif command == 'list_courses':
            list_courses()
        elif command == 'students_and_their_courses':
            list_students_and_their_courses()
        elif command == 'help':
            list_commands()
        elif command == 'students_most_attending':
            list_students_most_attending()


def main():
    print ('This is a program for operating with a database. This is the user interface.')
    list_commands()
    read_command()


if __name__ == '__main__':
    main()
