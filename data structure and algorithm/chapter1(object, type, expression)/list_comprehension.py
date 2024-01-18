# A common and very intuitive way to create lists from expressions is using list
# comprehensions. This allows us to create a list by writing an expression directly into the
# list, for example:

list = [1,3,5,7,9]
name = [i**4 for i in list if i%2!=0]
print(name)

l1 = [1, 2, 3, 4, 5, 6]

# l2 =[]
# for item in l1:
#     l2.append(item*item)

l2 = [i*i for i in l1 if i>2]
print(l2)

# List comprehensions can be quite flexible; for example, consider the following code. It
# essentially shows two different ways to performs a function composition, where we apply
# one function (x * 4) to another (x * 2). The following code prints out two lists
# representing the function composition of f1 and f2 calculated first using a for loop and
# then using a list comprehension

def f1(x): 
    return x*2
def f2(x):
    return x*4
lst = []
for i in range(16):
    lst.append(f1(f2(i)))
print(lst)
print([f1(x) for x in range(64) if x in [f2(j) for j in range(16)]])

# List comprehensions can also be used to replicate the action of nested loops in a more
# compact form. For example, we multiply each of the elements contained within list1 with
# each other:
    
list1 = [1,2,3,4],[5,6,7,8]

name = [i*j for i in list1[0] for j in list1[1]]

print("multiply two list with each other:",name)

# We can also use list comprehensions with other objects such as strings, to build more
# complex structures. For example, the following code creates a list of words and their letter
# count:

words = "muhammad maaz is the student of government superior science college".split()
name = [[word,len(word )] for word  in words ]

print(name)
