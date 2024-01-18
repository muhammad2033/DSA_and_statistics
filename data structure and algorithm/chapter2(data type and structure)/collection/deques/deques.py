from collections import deque


d = deque()
d.append(3)
d.append(1)
d.append(255)

print(d)

dq = deque("abc")  #create deque (['a','b','c' ])

dq.append('d') #append by default at the end (right)

dq.appendleft("n") #append by default at the beginning (left)

dq.extend("maaz") #add multiples item to the right

dq.extendleft("nothing") #add multiples item to the left
print(dq)

# We can use the pop() and popleft() methods for consuming items in the deque, for
# example:

dq.pop() # return and removes and item from the right

dq.popleft()# return and removes and item from the left

print(dq)

# We can also use the rotate(n) method to move and rotate all items of n steps to the right
# for positive values of the integer n, or left for negative values of n the left, using positive
# integers as the argument, for example

dq.rotate(4) #rotate all item 4 steps to the right

dq.rotate(-4) #rotate all item 4 steps to the left

print(dq)

# Note that we can use the rotate and pop methods to delete selected elements. Also worth
# knowing is a simple way to return a slice of a deque, as a list, which can be done as follows:
 
# A useful feature of deques is that they support a maxlen optional parameter that restricts
# the size of the deque. This makes it ideally suited to a data structure known as a circular
# buffer. This is a fixed-size structure that is effectively connected end to end and they are
# typically used for buffering data streams. The following is a basic example:


dq2=deque([])
for i in range(6):
    dq2.append(i)
    print(dq2)

# In this example, we are populating from the right and consuming from the left. Notice that
# once the buffer is full, the oldest values are consumed first, and values are replaced from
# the right. We will look at circular buffers again in Chapter 4, Lists and Pointer Structures, by
# implementing circular lists 