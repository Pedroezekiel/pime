class Animal:

    def __init__(self,name,age ):
        self.name = name
        self.age  = age
    def walking(self):
       return f"{self.name} can walk"
    def sleeping(self):
        return f"{self.name} can sleep"
    def eating(self):
         return f"{self.name} can eat"
class Dog(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self,words = "wof wof"):
        return f"{self.name} says {words}"
class Cat(Animal):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self,words ="meow meow"):
         return f"{self.name} says {words}"


kitten = Cat("kit", 5, "femal")