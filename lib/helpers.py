from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    '''The function should get all employees stored in the database, then print each employee on a new line.'''
    employees = Employee.get_all()
    for e in employees:
        print(e)


def find_employee_by_name():
    '''should prompt for a name and then find the Employee instance with that 
    name and print their information, or print an error message if the employee does not exist.'''
    name_ = input("Enter the employee's name: ")
    e = Employee.find_by_name(name_)
    print(e) if e else print(f'Employee {name_} not found')

def find_employee_by_id():
    '''should prompt for an id and then find the Employee instance with that id and print their 
    information, or print an error message if the employee does not exist.'''
    _id = input("Hey, enter the id of the employee: ")
    e = Employee.find_by_id(_id)
    print(e) if e else print(f'Employee of id {_id} not found.')

def create_employee():
    '''Prompt for and read in a name, job title, and department id.
        Create and persist a new Employee class instance, surrounding the code in a try/except 
        block in case an exception is thrown by the name, job_title, or department_id property setter methods.
        Print a message indicating that the Employee object was successfully created, or print an 
        error message if an exception is thrown.
    '''
    
    
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    _id = int(input("Enter the employee's department id: "))
    try:
        e = Employee.create(name, job_title, _id)
        print(f'Success: {e}')
    except Exception as exc:
        print("Error creating employee: ", exc)

def update_employee():
    '''
    Prompt for and read in the employee id.
    Print an error message if the employee is not in the database. If the employee is in the database, attempt to do the following steps within a try-except block to catch any exceptions, printing an error message if an exception is thrown.
    Prompt for a new name to update the name attribute (property setter may throw an exception).
    Prompt for a new job title to update the job_title attribute (property setter may throw an exception).
    Prompt for the employee's new department id to update the department_id attribute (property setter may throw an exception).
    Update the employee in the database.
    Print a success message after a successful update, or print an appropriate error message if an exception is thrown.
    '''
    id_ = int(input("Enter the employee's id: "))
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            job = input("Enter the employee's new job title: ")
            employee.job_title = job

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'employee {id_} not found')


def delete_employee():
    '''
    prompt for the employee id and delete the employee from the database 
    if it exists and print a confirmation message, or print an error message if the employee is not in the database.
    '''
    c
    if emp := Employee.find_by_id(id_):
        emp.delete()
        print(f'emp {id_} deleted')
    else:
        print(f'emp {id_} not found')


def list_department_employees():
    '''
    prompt for a department id.
    find the department with that id from the database.
    if the department exists in the database, get the department's employees (HINT: call the employees() instance method) and loop to print each employee's data on a separate line.
    if the department does not exist in the database, print an error message.
    '''
    id_ = int(input("Enter the department's id: "))
    department = Department.find_by_id(id_)
    print(department)
    
    if department := Department.find_by_id(id_):
        for employee in department.employees():
            print(employee)
    else:
        print(f'Department {id_} not found')