d = {"two":2, "three":3,"one":1,"four":4,"six":6,"five":5}

sorting = sorted(list(d.keys())) #it can be done bu defualt
# this sorts the list according to the letters 

print("sorting:",sorting) 

sorting = sorted(list(d.values()))
# this sorts the list according to the integers 

print("sorting:",sorting)

# (key argument )

sorting = sorted(list(d),key = d.__iter__)
 
# this sorts the list according to the rules  
print("sorting:",sorting)

# in list comprehension form 

sorting = [value for(key,value) in sorted(d.items()) ]
print("sorting:",sorting)


sorting = sorted(list(d),key = d.__getitem__,reverse= True)
 
# this sorts and reverse the list according to the rules  
print("sorting:",sorting)


