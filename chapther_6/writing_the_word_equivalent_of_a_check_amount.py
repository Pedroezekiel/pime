from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Person:
    name: str
    age: int = 16

    def is_minor(self):
        return self.age < 18


p1 = Person('John')
p2 = Person('Adeola')
print(p2 < p1)
