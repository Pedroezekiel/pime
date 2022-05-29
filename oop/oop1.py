se1 = ["Software Engineer", 'Max', 20, 'Junior', 5000]
se2 = ["Software Engineer", 'Lisa', 25, 'senior', 7000]


def code(se):
    print(f'{se[1]} is writing code')


# class
class SoftwareEngineer:
    # class attribute
    alias = "keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f'{self.name} is writing code')

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...........")

    def information(self):
        information = f"name ={self.name}, age = {self.age}, level = {self.level}, salary = {self.salary} "
        return information


# instance
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('lisa', 25, 'senior', 7000)
se2.code_in_language("python")
print(se1.information())
