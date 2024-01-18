# it is immutable 
set = [1,2,3,4,5,6]
a = frozenset(set)
print(set)

print(type(set))

# a.add(5)
# print(set) #immutable 

print(2 in set)

print(9 in set)

print('y' in set)

for i in set: #iteration
    print(i)
    
                            #UNION
x = {'a','b','c','d','e'}                              
y = {'d','e','f'}       

z =x|y  # for union 

print(z) 
                    #intersection   
z = x&y
print(z)      #inersection   

                # differences            
z = x-y
print(z)                

                    # or   
z = y-x
print(z)                

                    #isSubset
print(x>y)  #false coz the x doesnt have all elements in y 

z = {'a','b'}
                    
print(x>z)  #true coz the z has all elements in x                     
