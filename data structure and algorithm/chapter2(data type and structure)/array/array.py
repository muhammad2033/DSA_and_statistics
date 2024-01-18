import  array 

ba = array.array("i", range(10**2))

print("ba:",ba)

bl =('m', list (range(10**2)))
print("bl:",bl)

import sys

name = 100*sys.getsizeof(ba)/sys.getsizeof(bl)
print(" name :", name)