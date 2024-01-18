# (key argument )

d = {"two":2, "three":3,"one":1,"four":4,"six":6,"five":5}


sorting = sorted(list(d),key = d.__getitem__)
 
# this sorts the list according to the rules  
print("sorting:",sorting)

# in list comprehension form 

sorting = [value for(key,value) in sorted(d.items()) ]
print("sorting:",sorting)
