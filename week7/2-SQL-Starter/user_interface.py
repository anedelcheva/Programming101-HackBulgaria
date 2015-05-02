from manage_company import Company


class UserInterface:

    def __init__(self, database):
        self.company = Company(database)
        self.commands = {'list_employees', 'update_employee', 'monthly_spending',
        'yearly_spending', 'add_employee', 'delete_employee', 'help'}

    def list_employees(self):
        all_employees = self.company.list_employees()
        for row in all_employees:
            print ('{} - {} - {}'.format(row[0], row[1], row[2]))

    def monthly_spending(self):
        month_sum = self.company.monthly_spending()
        print ('The company is spending ${} every month!'.format(month_sum))

    def yearly_spending(self):
        year_sum = self.company.yearly_spending()
        print ('The company is spending ${} every year!'.format(year_sum))

    def add_employee(self):
        name = input('name>')
        salary = input('monthly_salary>')
        bonus = input('yearly_bonus>')
        position = input('position>')
        self.company.add_employee(name, salary, bonus, position)

    def delete_employee(self, ID):
        if self.company.person_in_db(ID):
            name = self.company.delete_employee(ID)
            print ('{} was deleted.'.format(name))
        else:
            print ('No person with this id.')

    def update_employee(self, ID):
        name = input('name>')
        salary = input('monthly_salary>')
        bonus = input('yearly_bonus>')
        position = input('position>')
        self.company.update_employee(ID, name, salary, bonus, position)

    def is_command(self, command):
        return command in self.commands

    def list_commands(self):
        for command in self.commands:
            print (command)

    def parse_command(self, command):
        return tuple(command.split(' '))

    def read_command(self):
        while True:
            user_input = self.parse_command(input('command>'))
            length = len(user_input)
            command = user_input[0]
            if not self.is_command(command):
                print ("No such command!")
            if length == 2:
                ID = int(user_input[1])
            if command == 'list_employees':
                self.list_employees()
            elif (command in ['update_employee', 'delete_employee']) and length < 2:
                print ("You didn't give an id.")
            elif command == 'update_employee':
                self.update_employee(ID)
            elif command == 'monthly_spending':
                self.monthly_spending()
            elif command == 'yearly_spending':
                self.yearly_spending()
            elif command == 'add_employee':
                self.add_employee()
            elif command == 'delete_employee':
                self.delete_employee(ID)
            elif command == 'help':
                self.list_commands()

def main():
    print ('''This is a database holding the employees in a company.
            You have the following commands:''')
    ui = UserInterface('company.db')
    ui.list_commands()
    ui.read_command()

if __name__ == '__main__':
    main()
