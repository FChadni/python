# Creating a function:
print("Creating user define function")
def example():
    print("test")
example()
print()

# Function Argument
print("Function Argument")
def example2(name):
    print("Hello", name)
example2("Tom")
print()

# Function Argument ~ Positional
print("Function Argument ~ Positional")
name = "Tom"
age = "25"
def example3(name, age):
    result = name + " is " + age
    return result
print("Name and Age:", example3(name, age))
print()

# Function Argument ~ Default
print("Function Argument ~ Default")
def sum(num1=5, num2=20):  # define defalut value in the argument
    total = num1 + num2
    return total
print("the sume is:", sum(1))
print()

# Function Argument ~ Keyword
print("Function Argument ~ Keyword")
def greet (name,message):
    print(name)
    print(message)
greet(message="how are you ", name="Janny")
print()

# Local Variable
print("Global Variable ~ created inside function")
def localVar(num1, num2):
    result = num1 + num2
    return result
print("Local variable only exit in function scope", localVar(2,5))
print()

# Global Variable
print("Global Variable ~ created outside function")
num2 = 5
def globalVar(num1):
    result = num1 + num2
    return result
print("Global variable exit both in and outside function scope",globalVar(5))
print()

# Change global message from inside function
message = "global keyword"
def globalKeyword():
    global message
    message = "global keyword changed"
    return message
print("Message inside function:", globalKeyword())
print("message outside function:", message)

