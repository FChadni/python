print()
print("********** similar to list but does not contain duplicate item nor in order **********")
print("********** set can be only created using immutable items (tuple, string, numbers) **********")
number_set = {1,5,6,7}
print("Number tuple:", number_set)
mixed_set = {2.5, "hey", 5, 5}
print("Mixed tuple: ", mixed_set)
empty_set = set()
print("Empty tuple: ", empty_set)
print()

#convert list to set
print("convert list to set")
number_set = set([1,5,6,7])
print("Number set: ", number_set)
print()

#add item to set
print("add item to set")
number_set.add(100)
print("Number set after add: ", number_set)
number_set.update(mixed_set, {200})
print("Number set after combining: ", number_set)
print()

#remove item from set
print("remove item from set")
number_set.remove(100) #remove returns error
print("Number set after remove: ", number_set)
number_set.discard(100) #discard returns none
print("Number set after discard: ", number_set)
print()

#Check if a item is in the list or not
print("Check if a item is in the set")
if 5 in number_set:
    print("true")
else:
    print("false")
print()

#iterating through list
print("iterating through set")
for number in number_set:
    print(number)
print()

#set operation
print("********** SET METHODS **********")
print()

#creating union of set
print("creating union of set")
unionSet = number_set.union(mixed_set)
unionSet2 = number_set | mixed_set
print(unionSet)
print(unionSet2)
print()

#find intersection of set
print("creating union of set")
intersectionSet = number_set.intersection(mixed_set)
intersectionSet2 = number_set & mixed_set
print(intersectionSet)
print(intersectionSet2)