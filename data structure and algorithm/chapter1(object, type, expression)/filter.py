# In this tutorial, we will learn about the Python filter() function with the help of examples.

# The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.

# Example

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Output: [2, 4, 6, 8, 10]

# Run Code
# filter() Syntax
# Its syntax is:

# filter(function, iterable)
# filter() Arguments
# The filter() function takes two arguments:

# function - a function
# iterable - an iterable like sets, lists, tuples etc.
# filter() Return Value
# The filter() function returns an iterator.

# Note: You can easily convert iterators to sequences like lists, tuples, strings etc.

# Example 1: Working of filter()

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)

# Run Code
# Output

# ('a', 'e', 'i', 'o')
# Here, the filter() function extracts only the vowel letters from the letters list. Here's how this code works:

# Each element of the letters list is passed to the filter_vowels() function.
# If filter_vowels() returns True, that element is extracted otherwise it's filtered out.
# Note: It's also possible to filter lists using a loop, however, using the filter() function is much more cleaner.

# Example 2: Using Lambda Function Inside filter()

numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers 
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Run Code
# Output

# [2, 4, 6]
# Here, we have directly passed a lambda function inside filter().

# Our lambda function returns True for even numbers. Hence, the filter() function returns an iterator containing even numbers only.

# Example 3: Using None as a Function Inside filter()

# random list

random_list = [1, 'a', 0, False, True, '0']

filtered_iterator = filter(None, random_list)

#converting to list
filtered_list = list(filtered_iterator)

print(filtered_list)

# Run Code
# Output

# [1, 'a', True, '0']
# When None is used as the first argument to the filter() function, all elements that are truthy values (gives True if converted to boolean) are extracted.

