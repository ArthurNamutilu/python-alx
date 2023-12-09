# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


# child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")


dog1 = Dog("Bosco")
cat1 = Cat("pss")

dog1.speak()
cat1.speak()
