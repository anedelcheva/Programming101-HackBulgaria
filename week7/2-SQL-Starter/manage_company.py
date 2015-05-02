import sqlite3


class Company:

    def __init__(self, database):
        self.database = sqlite3.connect(database) # sqlite3.Connection object
        self.cursor = self.database.cursor() # sqlite3.Cursor object

    def create_tables(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        monthly_salary INTEGER,
        bonus INTEGER,
        position TEXT)'''
        self.cursor.execute(create_table_query)

    def list_employees(self):
        self.cursor.execute('SELECT id, name, position FROM employees')
        all_employees = self.cursor.fetchall()
        return all_employees

    def monthly_spending(self):
        self.cursor.execute('SELECT monthly_salary FROM employees')
        salaries = self.cursor.fetchall()
        month_sum = 0
        for salary in salaries:
            month_sum += salary[0]
        return month_sum

    def yearly_spending(self):
        month_sum = self.monthly_spending()
        return 12 * month_sum

    def add_employee(self, name, salary, bonus, position):
        self.cursor.execute('''INSERT INTO employees
            (name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)''', (name, salary, bonus, position))
        self.database.commit()

    def person_in_db(self, ID):
        self.cursor.execute('SELECT id FROM employees')
        ids = self.cursor.fetchall()
        id_nums = []
        for id_num in ids:
            id_nums.append(id_num[0])
        if ID in id_nums:
            return True
        else:
            return False

    def delete_employee(self, ID):
        self.cursor.execute('SELECT name FROM employees WHERE id=?', (ID,))
        name = self.cursor.fetchone()
        self.cursor.execute('DELETE FROM employees WHERE id=?', (ID,))
        self.database.commit()
        return name[0]

    def update_employee(self, ID, name, salary, bonus, position):
        self.cursor.execute('''UPDATE employees SET name=?, monthly_salary=?,
            yearly_bonus=?, position=? WHERE id=?''', (name, salary, bonus, position, ID))
        self.database.commit()

c = Company('company.db')
# c.create_tables()
#print (c.cursor)
#print (c.list_employees())
#print (c.monthly_spending())
# c.delete_employee(3)
# print (c.person_in_db(6))
# print (c.person_in_db(2))
# c.update_employee(2, 'Aneta Nedelcheva', 3000, 1000, 'Junior Developer')
# print (c.list_employees())
