# from collections import Counter

# c1 = Counter()
# c1.update("name")
# print("updation",c1)

# c1.update({"a":5,"m":6})
# print("updation",c1)

# c1.update({"a":-2,"m":-3,'e':-1,"n":2})
# print("updation:",c1)

# # sorting the order 
# print(sorted(c1.elements())) # sorted and spread the all letters in dictionary formet (iterator )
# #  list in order 

# c2 =c1.most_common()
# print("order :",c2)

# # subtraction 

# c3 = c1.subtract({"a":2,"m":3})
# print("subtracion :",c1)   #it's like updation, will be done in the first step( initializtion one) 


from collections import OrderedDict



odr = OrderedDict()
odr['one'] = 1
odr['two'] = 2

odr.update({'three':3})  #mutable data structure
odr['four'] = 4
odr['five'] = 5
odr['six'] = 6
odr['seven'] = 7
odr['eight'] = 8

print(odr)

odr2 = OrderedDict()

odr2['two'] = 1
odr2['one'] = 2

print(odr2)

new = odr == odr2  # false coz both are not equal

print(new)