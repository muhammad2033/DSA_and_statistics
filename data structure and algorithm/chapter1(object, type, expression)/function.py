# To have a look at how this works, let's define a simple function

def greet(langaue):
    if langaue=='eng':
        return"this is an English language "
        
    elif langaue =='urdu':
        return"this is a urdu language"
     
    else:
        return"this is a pushto language"
        
# Since user-defined functions are objects, we can do things such as include them in other
# objects, such as lists:

        
l =[greet('eng'),greet('urdu'),greet('pushto')]
print(l[1])


# Functions can also be used as arguments for other functions. For example, we can define the
# following function:

def callf(f):
    lang = 'eng'
    return (f(callf))
print(callf(greet))

# Here, callf() takes a function as an argument, sets a language variable to 'eng', and then
# calls the function with the language variable as its argument. We could see how this would
# be useful if, for example, we wanted to produce a program that returns specific sentences in
# a variety of languages, perhaps for some sort of natural language application. Here we have
# a central place to set the language. As well as our greeting function, we could create
# similar functions that return different sentences. By having one point where we set the
# language, the rest of the program logic does not have to worry about this. If we want to
# change the language, we simply change the language variable and we can keep everything
# else the same.