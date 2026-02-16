class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee, Person):
    def __init__(self, name, age, emp_id, salary, department):
        Employee.__init__(self, name, age, emp_id, salary)
        self.department = department

    def show_manager(self):
        self.show_person()
        self.show_employee()
        print("Department:", self.department)

m1 = Manager("Rahul", 35, 101, 50000, "HR")
m1.show_manager()