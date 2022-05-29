# inherits, extends, override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")


class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding")

    def debugging(self):
        print(f"{self.name} is debugging")


class Designer(Employee):
    def drawing(self):
        print(f"{self.name} is drawing")

    def work(self):
        print(f"{self.name} is designing")


se = SoftwareEngineer("mark", 12, 7000, "junior")
# se.work()

d = Designer("phillp", 10, 10_000)
# d.work()

# Polymorphism

employees = [SoftwareEngineer("mark", 20, 7000, "junior"),
             SoftwareEngineer("lisa", 17, 7000, "senior"),
             Designer("phillp", 25, 10_000)]


def motive_employee(employees):
    for employee in employees:
        employee.work()


motive_employee(employees)
