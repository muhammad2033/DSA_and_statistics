from collections import Counter 

c1 = Counter("muhammad maaz") # it counts the each alphabet in dictionary format
print(c1)

c2 = Counter('2,3,4,5,6')  # it applies on integer as well 
print("counter :",c2)

                            # initialization 

c3 = Counter()  # updation must be here , should be printed this 

c3.update('name')

print("updation:",c3)


print("a optimization: ", c3.keys())
print("a optimization: ", c3.values())


c3.update({'a':5,'m':4}) # it must be inside the curly bracket, coz it's dictionary


print("a optimization: ", c3)
print("Most_common",c3.most_common()[0][0])  #the first [0] means the first pair one and last [0] means the first key of the pair

print("new", c3)

print("element:",(list(c3.elements())))

# # firstly 'a' had one value then we optimize(5 more) upto 6 
# # and furthermore 'm' had one value too then we optimize(4 more) upto 5


# # in iteration form 


new = Counter("muhammad is the famous name in the world ") 
print(new)

for item in new :
    print(" iterator : %s  :  %d"%(item,new[item]))
    
print(new['x'])   #xero