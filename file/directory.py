# folder/directory (os module) ~ stores and organizes multiple files and sub-directory
import os

print("Location of the path to current file")
current_dir = os.getcwd()
print(current_dir)
print()

print("Change file path")
# os.chdir("/Users/farjanachadni/Documents/python/file/directory.py")
print()

print("Listing all directories")
print(os.listdir())
print()

print("Create new directory")
# os.mkdir("test")
# os.mkdir("../datatype/test")
print()

print("Renaming a directory or file")
# os.rename("test", "test-new")

print("Removing a file")
# os.remove("test-new")

print("Removing a directory")
# os.rmdir("test-new")
