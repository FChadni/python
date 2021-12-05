print()
print("********** similar to list but immutable cannot add or remove item **********")
number_tuple = (1,5,6,7)
print("Number tuple:", number_tuple)
mixed_tuple = (2.5, "hey", -5, 5)
print("Mixed tuple: ", mixed_tuple)
empty_tuple = ()
print("Empty tuple: ", empty_tuple)
print()

#to get length of list:
print("Length of tuple: ", len(number_tuple))
print()

#access list element and negative indexing
print("First element of the tuple: ", number_tuple[0])
print("Last element of the tuple: ", number_tuple[-1])
print()

#slicing list, first intex is inclusive and last index is exclusive
print("First three element of the tuple: ", number_tuple[0:3])
print()

#Check if a item is in the list or not
print("Check if a item is in the tuple")
if 5 in number_tuple:
    print("true")
else:
    print("false")
print()

#iterating through list
print("iterating through tuple")
for number in number_tuple:
    print(number)
print()

#Tuple Methods
print("********** TUPLE METHODS **********")
print()