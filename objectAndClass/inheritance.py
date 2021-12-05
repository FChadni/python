# Inheritance ~ allows to inherit attributes and methods from a parent class to child classes
# Parent class (Vehicle) ~> Derived classes (car and motorcycle)

class Animal:
    def eat(self):
        print("I enjoy eating")

class Dog(Animal):
    def bark(self):
        print("I enjoy barking")

dog1 = Dog()
dog1.bark(), dog1.eat()