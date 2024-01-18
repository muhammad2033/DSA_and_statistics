# sorting argument 

d = {"two":2, "three":3,"one":1,"four":4,"six":6,"five":5}

sorting = sorted(list(d),key = d.__getitem__,reverse= True)
 
# this sorts and reverse the list according to the rules  
print("sorting:",sorting)

d2 ={'one':'uno' , 'two':'deux', 'three':'trois', 'four': 'quatre', 'five':
'cinq', 'six':'six'}
#  for key of d2 and d   
name = sorted(d2, key = d.__getitem__)
print(name)

# for values of d2
name = [d2[i] for i in sorted(d2,key= d.__getitem__)]
print("sorting the values if string:",name)
#  another method 

def sorting(string):
    return (string [len(string)-1])

name = sorted(d2.values(), key = sorting, reverse=True) 

print("values of string: ", name)