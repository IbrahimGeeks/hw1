class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Some animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Гав гав")


class Cat(Animal):
    def make_sound(self):
        print("Мияу")


dog = Dog("Полет", 3)
kitty = Cat("Парик", 1)

animals = [dog, kitty]

for animal in animals:
    print("Name:", animal.get_name())
    print("Age:", animal.get_age())
    animal.make_sound()
    print()

kitty.set_age(2)

print("New age of kitty:", kitty.get_age())