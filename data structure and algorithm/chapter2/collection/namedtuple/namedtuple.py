from collections import namedtuple
# In addition to the inherited tuple methods, the named tuple also defines three methods of
# its own, _make() , asdict(), and _replace. These methods begin with an underscore to
# prevent potential conflicts with field names. The _make() method takes an iterable as an
# argument and turns it into a named tuple object, for example:



space = namedtuple('Space' ,  'x y z')

s1 =  space(x = 100, y = 2.9999 , z = 2.2222)  # we can use the space(10,2.9,2.2   )

print("namedtuple: ",s1.x *s1.y *s1.z)

# The _asdict method returns an OrderedDict with the field names mapped to index keys
# and the values mapped to the dictionary values, for example:

space2 = namedtuple('Space2' ,  'x def z', rename =  True)

s2 =  space2(10, 2.9 , 2.2)  # we can use the space(10,2.9,2.2  )

# print("namedtuple: ",s2.def) # error , invalid index 


print("namedtuple: ",s2._1) #  with underscore _1

# The _replace method returns a new instance of the tuple, replacing the specified values,
# for example

sl = [3,4,5]  # x wil assign 3 , y 4 and z will 5

print(space._make(sl))   #Space(x=100, y=2.9999, z=2.2222)

print(space._asdict(s1))  #dictionary ({'x': 100, 'y': 2.9999, 'z': 2.2222})

print(s2._replace(x = 9 , z = 6))  # for s1  space2(x=10, _1=2.9, z=2.2)