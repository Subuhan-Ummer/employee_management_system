# employee_management_system


This project is a simple Employee Management System in Python, designed to demonstrate basic object-oriented programming concepts. It includes an `Employee` class with attributes and methods to manage an employee’s details.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Classes and Structure](#classes-and-structure)
- [Usage](#usage)

---

## Overview

The Employee Management System defines an `Employee` class within an external module named `employee.py`. The class allows you to manage basic employee data such as name and salary and includes methods to retrieve these details.

## Features

- Create an employee with a name and salary.
- Retrieve employee details, such as name and salary, using class methods.

## Classes and Structure

- **Employee**: This class represents an employee with two main attributes:
  - `name` (str): Stores the employee's name.
  - `salary` (float): Stores the employee's salary.

  **Methods**:
  - `get_name()`: Returns the employee's name.
  - `get_salary()`: Returns the employee's salary.

## Usage

To use this module, import it into a Python script and create an instance of the `Employee` class.

1. First, import the `Employee` class from `employee.py`:

    ```python
    from employee import Employee
    ```

2. Create an `Employee` instance and access its methods:

    ```python
    # Create an instance of Employee
    emp = Employee("John Doe", 50000)

    # Display the employee's name and salary
    print("Employee Name:", emp.get_name())
    print("Employee Salary:", emp.get_salary())
    ```


