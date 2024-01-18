a = 11 ; b = 22   
def scope():
    global a
    a = 13; b = 25

    print(a)   #13
    print(b)    #25
 
scope()    

print(a)  #13
print(b)  #22


# basically, local is always used inside the function and global is outside the function
 
# but we can use global inside the function with the help of key_word global