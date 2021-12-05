print("********** List is a sequence of item in order **********")
number_list = [1,5,6,7]
print("Number List:", number_list)
mixed_list = [2.5, "hey", -5, 5]
print("Mixed list: ", mixed_list)
empty_list = []
print("Empty List: ", empty_list)
print()

#to get length of list:
print("Length of list: ", len(number_list))
print()

#access list element and negative indexing
print("First element of the list: ", number_list[0])
print("Last element of the list: ", number_list[-1])
print()

#slicing list, first intex is inclusive and last index is exclusive
print("First three element of the list: ", number_list[0:3])
print()

#modify items in list
number_list[0] = 5
print("Number List after modify:", number_list)
number_list[0:2] = 5,25
print("Number List after modify:", number_list)
print()

#Check if a item is in the list or not
print("Check if a item is in the list")
if 5 in number_list:
    print("true")
else:
    print("false")
print()

#iterating through list
print("iterating through list")
for number in number_list:
    print(number)
print()

#List Methods
print("********** LIST METHODS **********")
print()

#copy the list before modifying
number_list1 = number_list.copy()
print("Copy of number list: ", number_list1)

#Add an item to a list
number_list.append(100)
print("Number List after append:", number_list)
#add an item to a specific index in the list
number_list.insert(1, 100)
print("Number List after insert:", number_list)

#Remove an item to a list
number_list.remove(100)
print("Number List after remove:", number_list)
