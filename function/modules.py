# Module ~ file that contains python code that can be used in program
import math as m # math module

print("Math module directory")
print(dir(m))
print()

print("Use math module")
num = 25
result = m.sqrt(num)
print(result)
print()

print("Remane module 'as <name>'")
print("math is renamed to m")
print()

print("To import a single or multiple functions")
print("'from import math sqrt' ~ use 'sqrt(num)' no need for dot")
print()

print("Create custom Modules ~ see main file")
import main
add = main.add(5, 5)
sub = main.sub(5, 5)
print(add, sub)
