from collections import ChainMap
default={"theme" :"defualt", "langauge" :"eng", "showindex": True ,"showfooter":True }
name = ChainMap(default)
print(name)

name1 = name.new_child({"theme":"busky"})
print(name1['theme'])




list = [1,2,9,4,5,6,7]

print(sorted(list))


# it is used to encapsulate multiple dictionaries into a single one   

d1 = {"maaz":4,"haris":5}
d2 = {"thread":6,"pondering":9}
name = ChainMap(d1,d2)
print(name['haris'])