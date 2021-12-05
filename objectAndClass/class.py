# Object Oriented Programming(OOP) ~ Object allows to organize related data together thus allowing structured code
#
# Steps to Creating Objects:
# define a class ~ student (class contain description ~ name, grade, check_pass_fail)
# Create Object ~ student1 and student2 ()
# In objects variables are called attributes and functions are called methods
#
# init method ~ gets automatically gets called everytime objects are created.

print("Creating a class")  # creating a class

class Student:
    print("\ncreating method inside class")  # create method inside class

    def check_pass_fail(self):
        if self.grade >= 50:
            return "Passed"
        else:
            return "Failed"

    print("\ncreating attributes inside class")  # create method inside class

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

print("\nobjects of student class\n")  # objects of the student class
student1 = Student("Janny", 90)
student2 = Student("Jan", 49)
# Manually assigning attributes are not considered good practice
# student1.name = "Janny"
# student1.grade = 90
print("Example 1")
print("Name:", student1.name, "Grade:", student1.grade, "Pass or fail:", student1.check_pass_fail())
print("Name:", student2.name, "Grade:", student2.grade, "Pass or fail:", student2.check_pass_fail())


# Example of using class and objectAndClass
print("\nExample 2")
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, num):
        real = self.real + num.real
        img = self.img + num.img
        result = Complex(real, img)
        return result


num1 = Complex(5,5)
num2 = Complex(10,10)
result = num1.add(num2)
print(result.real, result.img)

print("\nExample 3")
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

t1 = Triangle(3,4,5)
print(t1.perimeter())