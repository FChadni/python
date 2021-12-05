# Lambda Function ~ single line functions defined without name.

def double(num):  # normal function
    return num*2
print("Normal function result:",double(5))

doubleLambda = lambda num: num*2
print("Lambda function result:", doubleLambda(5))

greater = lambda a, b: a if a > b else b
print("Multiple argument lambda:", greater(5, 25))
print()

# Lambda functions are used more with python build-in functions
print("sort a list by its length")
names = ['aaaa', 'ggggggg', 'zzzzz', 'jjjj', 'tttt', 'aaaaa']
names.sort(key=lambda x: len(x))
print(names)
