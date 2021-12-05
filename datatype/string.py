print("Introduction to strings: ")
print("Creating string: ")
    #Strings can be created in python using 'single', "double" and """triple""" quote.
    #This makes it easy to store all kinds of text.

message = "hello human."
print(type(message)) #to see data type of variable
message2 = 'hello human single quote'
apostrophe = "apostrophe's method 1"
apostrophe2 = 'apostrophe\'s method 2.'
doubleQuote = '"double quote" method 1.'
doubleQuote2 = "\"double quote\" method 2."
tripleQuote = """let's test this out "do you think it will work." """
print(message)
print(message2)
print(apostrophe)
print(apostrophe2)
print(doubleQuote)
print(doubleQuote2)
print(tripleQuote)
print()

print("Accessing string characters: ")
print(message[0])  #print first character in the string.
print(message[-1]) #print last character in the string.
print()

print("Slicing string: ")
print(message[:5])
print(message[1:5])
print(message[0:])
print()

print("String Operation: ")
combine = message + " " + message2
mul = message * 2
print(combine)
print(mul)
print()

print("String length: ")
print("size of the string: ", len(message))
print()

print("Check a character in string: ")
if "h" in message:
    print("true")
print()

print("String Iteration: ")
for character in message:
    print(character)
print()

print("String Methods: ")
lowCase = message.lower()
lowCase2 = message.casefold()
upCase = message.upper()
print("Lower Case: ", lowCase, "Lower Case2: ", lowCase2, "Upper Case: ", upCase)
findIndex = message.find("o")
print(findIndex)
print()

#Capitalize() converts first character to uppercase letter and lowercases all other characters.
capitalizeStr = message.capitalize()
print("Capitalize Str: ", capitalizeStr)
print()

#center() returns padded string with the specified character: string.center(width, fillchar)
centerStr = message.center(14, '*')
print("Center Str: ", centerStr)
print()

#count() returns the number of occurrences of a substring in the given string.
#string.count(substring, start, end)
countStr = message.count('h')
print("Count Str: ", countStr)
print()

#encode() returns an encoded version of the given string.
encodeStr = message.encode()
print("Encode Str: ", encodeStr)
print()

#endswith() returns True if a string ends with the specified suffix.
endStr = message.endswith('hello')
print("Endswith Str: ", endStr)
print()

#startswith() returns True if a string starts with the specified prefix(string).
staStr = message.startswith("hello")
print("Startswith Str: ", staStr)
print()

#expandtabs() returns a copy of string with all tab characters '\t' replaced with
# whitespace characters until the next multiple of tabsize parameter.
expStr = message.expandtabs()
print("Expandtabs Str: ", expStr)
print()

#index() returns the index of a substring inside the string (if found).
# The only difference is that find() method returns -1 if the substring
# is not found, whereas index() throws an exception.
indStr = message.index("hello")
print("index Str: ", indStr)
print()

#isalnum() returns True if all characters in the string are alphanumeric (either alphabets or numbers).
alumStr = message.isalnum()
print("alnumStr: ", alumStr)
print()

#isalpha() returns True if all characters in the string are alphabets.
alphaStr = message.isalpha()
print("alphaStr: ", alphaStr)
print()

#isdigit() returns True if all characters in a string are digits.
digitStr = message.isdigit()
print("digitStr: ", digitStr)
print()

#isdecimal() returns True if all characters in a string are decimal characters.
decimalStr = message.isdecimal()
print("decimalStr: ", decimalStr)
print()

#isnumeric() returns True if all characters in a string are numeric characters.
numericStr = message.isnumeric()
print("numericStr: ", numericStr)
print()

#isidentifier() returns True if the string is a valid identifier in Python.
identiferStr = message.isidentifier()
print("identifierStr: ", identiferStr)
print()

#islower() returns True if all alphabets in a string are lowercase alphabets.
lowerStr = message.islower()
print("lowerStr: ", lowerStr)
print()

#isupper() returns True if all alphabets in a string are uppercase alphabets.
upperStr = message.isupper()
print("upperStr: ", upperStr)
print()

#isprintable() returns True if all characters in the string are printable or the string is empty.
printableStr = message.isprintable()
print("printableStr: ", printableStr)
print()

#isspace() returns True if there are only whitespace characters in the string.
spaceStr = message.isspace()
print("spaceStr: ", spaceStr)
print()

#join() string method returns a string by joining all the elements of an iterable
# (list, string, tuple), separated by a string separator.
joinStr = " ".join(message)
print("joinStr: ", joinStr)
print()

#lstrip() method returns a copy of the string with leading characters removed
# (based on the string argument passed).
stripStr = message.lstrip('hello')
print("stripStr: ", stripStr)
print()

#partition() splits the string at the first occurrence of the argument string and
# returns a tuple containing the part the before separator, argument string and
# the part after the separator.
splitStr = message.partition('hello')
print("splitStr: ", splitStr)
print()

#replace() replaces each matching occurrence of the old character/text in the
# string with the new character/text.
#old substring, new substring, count (optional) the number of times replace
replaceStr = message.replace('hello', 'hey')
print("replaceStr: ", replaceStr)
print()

#rfind() method returns the highest index of the substring (if found).
#If not found, it returns -1.
findStrIndex = message.rfind('l')
print("findStrIndex: ", findStrIndex)
print()

#rindex() returns the highest index of the substring inside the string (if found).
# If the substring is not found, it raises an exception.
indexStrIndex = message.rindex('l')
print("indexStrIndex: ", indexStrIndex)
print()