#main.py

from employee import Employee

#creating an instance of Employee
emp = Employee("John Doe", 50000)

print("Employee Name : ", emp.get_name())
print("Employee Salary : ", emp.get_salary())