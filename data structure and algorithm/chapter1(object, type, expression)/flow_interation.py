# There are two main ways of controlling
# the flow of program execution, conditional statements and loops.

# The if, else, and elif statements control the conditional execution of statements. The
# general format is a series of if and elif statements followed by a final else statement:

x='one'
if x==0:
    print('False')
elif x==1:
    print('True')
else:
    print('Something else')
#prints 'Something else'


# The other way of controlling program flow is with loops. They are created using the while
# or for statements, for example:

a = 0
while a<5:
    print(f"{a} :",a)
    a =a+1
    
# and for loop 

for i in range(4):
 
    
    print(id(i))