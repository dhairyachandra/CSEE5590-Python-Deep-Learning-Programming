# Parent Employee class
class Employee:

    # Count number of employees
    noOfEmployee = 0

    # Store salary of all employees
    tSalary = 0

# Constructor of parent class
    def __init__(self):
        self.name = input('Name: ')
        self.family = input('Family: ')
        self.salary = int(input('Salary: '))
        self.department = input('Department: ')
        Employee.noOfEmployee += 1
        Employee.tSalary += int(self.salary)

# Function to return data of employee

    def empDetails(self):
        empDetails = {}
        empDetails['Employee'] = Employee.noOfEmployee
        empDetails['Name'] = self.name
        empDetails['Family'] = self.family
        empDetails['Salary'] = self.salary
        empDetails['Department'] = self.department
        return empDetails

# Function for finding Average of salaries
    def avgSalary (self):
        avg = Employee.tSalary/Employee.noOfEmployee
        return avg
