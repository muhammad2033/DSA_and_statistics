from collections import defaultdict
from collections import OrderedDict
odr = OrderedDict()
odr['one'] = 1
odr['two'] = 2


odr.update({'three':3})  #mutable data structure
print(odr)

kv = ([('one', 1), ('two', 2), ('three', 3)])

odr.update(kv)
print(odr)
for k , v in odr.items():
    print(k ,v)

def isprimary(c):
    if (c == 'red') or (c == 'blue') or (c == 'green'):
        return True
    else:
        return False
    
odr3 = OrderedDict(sorted(odr.items(), key = lambda t : (4*t[1])-t[1]**2))
print(odr3.values())


# now we are about to start defaultdict 


dd = defaultdict(int)
print("defualtDict:",dd)


words = str.split("the blue looks like green and green looks like red ,but i like red , green and blue ")
for word in words:
    dd[word]+=1
print(dd)

dd2 = defaultdict(bool)
for word in words:
    dd2[word] = isprimary(word)
# whatever is given in the condition those things will be printed 
print(dd2)    

odr = defaultdict(int)
odr['one'] = 1
odr['two'] = 2

print(odr['c'])
    