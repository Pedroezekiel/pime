class Person:
    ID = 0

    def __init__(self, first_name, last_name, year, month, day, age):
        self.first_name = first_name
        self.last_name = last_name
        # self.age = age
        self.year = year
        self.month = month
        self.day = day
        Person.ID += 1

    def repr(self):
        return f"<Person: {self.first_name}"

    def str(self):
        return f"<Person: {{name={self.first_name}, {self.last_name}, age={self.age}}}"

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, year):
        if self.age < 18:
            raise ValueError("This website is info is strictly for 18+")
        self.age = 2022 - year


    @age.deleter
    def age(self):
        print("Age deleted")
        del self.age

    @classmethod
    def get_nun_of_id(cls):
        return cls.ID

    @staticmethod
    def get_age(age):
        return age


p1 = Person("John", "Doe", 1990, 1, 1, 18)
print(p1.ID)

