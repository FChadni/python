print()
print("********** collection of key value pair {key:value} **********")
print("********** key must be unique **********")
number_dic = {"one": 1, "five": 5, "six": 6, "seven": 7}
print("Number tuple:", number_dic)
mixed_dic = {"float": 2.5, "string": "hey", "integer": 5}
print("Mixed tuple: ", mixed_dic)
empty_dic = {}
print("Empty tuple: ", empty_dic)
print()

#access dictionary element
print("value of the given key: ", number_dic["one"])
# print("First element of the list: ", number_dic["two"]) #raises error use get to avoid
print("value of the given key: ", number_dic.get("two"))
print()

#Check if a item is in the list or not
print("Check if a item is in the list")
if "one" in number_dic:
    print("true")
else:
    print("false")
print()

#iterating through dictionary
print("iterating through dictionary")
for key in number_dic:
    print(key, ":", number_dic[key])
print()

#add an item to dictionary
print("add an item to dictionary")
number_dic["two"] = 2
print("Number List after insert:", number_dic)
print()

#remove an item to dictionary
print("remove an item from dictionary")
number_dic.pop("two")
print("Number dic after pop:", number_dic)
print()

#Dictionary Methods
print("********** DICTIONARY METHODS **********")
print()