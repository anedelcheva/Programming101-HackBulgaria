import sqlite3


create_table_query = '''
CREATE TABLE IF NOT EXISTS employees(
id INTEGER PRIMARY KEY,
name TEXT,
monthly_salary INTEGER,
yearly_bonus INTEGER,
position TEXT
)'''

db = sqlite3.connect('company.db')
c = db.cursor()
c.execute(create_table_query)

name1 = 'Ivan Ivanov'
salary1 = 5000
bonus1 = 10000
position1 = 'Software Developer'

name2 = 'Rado Rado'
salary2 = 500
bonus2 = 0
position2 = 'Technical Support Intern'

name3 = 'Ivo Ivo'
salary3 = 10000
bonus3 = 100000
position3 = 'CEO'

name4 = 'Petar Petrov'
salary4 = 3000
bonus4 = 1000
position4 = 'Marketing Manager'

name5 = 'Maria Georgieva'
salary5 = 8000
bonus5 = 10000
position5 = 'COO'

workers = [
(name1, salary1, bonus1, position1),
(name2, salary2, bonus2, position2),
(name3, salary3, bonus3, position3),
(name4, salary4, bonus4, position4),
(name5, salary5, bonus5, position5)
]

c.executemany('''INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', workers)

db.commit()
