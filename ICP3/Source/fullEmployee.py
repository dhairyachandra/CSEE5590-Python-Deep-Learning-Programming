
from employee import Employee

# Inheriting data from Parent class
class fullEmployee(Employee):
    def __init__(self):
        Employee.__init__(self)

# Instance of Parent class
emp = Employee()
print(emp.empDetails())

# Instance of child class
fullEmp = fullEmployee()
print(fullEmp.empDetails())

print('First Employee Name: ', emp.name)
print('Second Employee Name: ', fullEmp.name)

print("Number of Employees: ", Employee.noOfEmployee)
# Accessing data from child class
print('Average Salary: $', fullEmp.avgSalary())
