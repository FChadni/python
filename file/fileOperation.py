# Files ~ named locations on storage device for recording data
# File Mode
# "r" ~ read mode ~ opens a file in read mode by default
# "w" ~ write mode ~ opens file for writing, creates new file if does not exist, clears content of file if exists
# "a" ~ append mode ~ opens file for appending at the end of file and creates a new file if does not exist

# Open File
print("Open File")
file = open("message.txt", "r")
content = file.read()
print(content)
file.close()
print()

print("Read certain character of file")
file = open("message.txt", "r")
content = file.read(7)
print(content)
more_content = file.read(12)
print(more_content)
file.close()
print()

print("Error handling using try and finally")
try:
    file = open("message.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()

print("Error handling using with which automatically closes the file")
with open("message.txt", "r") as file:
    content = file.read()
    print(content)

print("Writing to file")
with open("message2.txt", "w") as file:
    file.write("Well this file will get created since it does not exist.")

print("Appending additional data to end of file")
with open("message.txt","a") as file:
    file.write("\nLets see if this gets added to end of the file.")

print("Readlines ~ content of a line")
with open("message.txt","r") as file:
    lines = file.readlines()
    print(lines)

print("Readlines ~ content of a line")
with open("message2.txt", "w") as file:
    lines = ['line1\n', 'line2\n', 'Line3']
    file.writelines(lines)
