# Syntax Errors ~
# Exception ~

# Exception Handling
print("Exception Handling using try except block")
try:
    num = 10
    dem = 0
    print(num/dem)
except ZeroDivisionError:
    print("Denominator cannot be 0")
print("Program Ends")
print()

# Multiple Exception Handling
print("Multiple Exception Handling using try except block")
try:
    num = 10
    dem = 0
    print(num/dem)
    lst = [1,2,3]
    print(lst[8])

except ZeroDivisionError:
    print("Denominator cannot be 0")
except IndexError:
    print("Index cannot be greater than the list")
print("Program Ends")
print()

# Exception Handling
print("Exception Handling using try except and finally block")
try:
    print(5/0)
except:
    print("cannot divide by 0")
finally:
    print("always printed")
print()

# Custom Exception Handling
print("Custom Exception Handling")
