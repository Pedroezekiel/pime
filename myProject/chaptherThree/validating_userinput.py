class Dog:
    species = "Canis Familiars"

    def ___init___(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, words):
        return f"{self.name} barks {words}"


class Philo(Dog):
    def speak(self, words="Arf"):
        return super().speak(words)

    pass


class Bulldog(Dog):
    pass


class GodenRetriever(Dog):
    def speak(self, words="Bark"):
        return f"{self.name} bark {words}"



buddy = Philo("Buddy", 7)
print(buddy.name)
print(buddy.speak("wof wof"))
print(type(buddy))
jim = Bulldog("jim", 5)
print(jim.speak("worf worf"))

# philo = Dog("Philo", 5, "Bulldog")
# print(philo.speak("Bow Bow"))
# print(philo.species)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, num):
        self = self + num
        return self


blue_car = Car("blue", 5)
red_car = Car("red", 30_000)
blue_car.mileage = Car.drive(blue_car.mileage, 100)
print(blue_car.mileage)
print(f"The {blue_car.color} has {blue_car.mileage} miles.")
print(f"The {red_car.color} has {red_car.mileage} miles.")
