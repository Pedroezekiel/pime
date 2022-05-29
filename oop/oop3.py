class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = 400
        self._number_of_bugs_solved = 0

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):
        # check value,enforce constraints
        self._salary = self._calculate_salary(base_value)

    def code(self):
        self._number_of_bugs_solved += 1

    def _calculate_salary(self, base_salary):
        if self._number_of_bugs_solved < 10:
            return base_salary
        if self._number_of_bugs_solved < 100:
            return base_salary * 2
        if self._number_of_bugs_solved < 1000:
            return base_salary * 3


se = SoftwareEngineer("Max", 30)

# se.set_salary(1200)
# print(se.get_salary())

for i in range(70):
    se.code()
se.set_salary(1000)
print(se.get_salary())
