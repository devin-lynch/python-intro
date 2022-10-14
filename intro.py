# I am a comment -- will not be executed

# i am a
# multiline
# comment

'''
I am a docstring
'''

"""
I am also a doc string
"""

# use the built in print function for output
print('Hello, Spam!')

# ctrl + d leaves the python3 repl

# python functions start with the 'def' keyword
def greeting(name):
    # this comment is tabbed in to the function scope
    print("Hello", name, "how are you liking python?")

# greeting('Gabe')

# python_variables_use_snake_case
# variable names use snake_case
# function names use snake_case

# # define a variable (no variable declaration keyword) (they work as a 'let' -- 'const' does not exist in python)
# my_variable = 'spam'
# print(my_variable)
# my_variable = 'eggs'
# print(my_variable)
# # there is no const, but convention among python programmers indicates consts WITH_CAPS
# MY_CONST = 'do not change me'
# # MY_CONST = 'will this work?'

# ## # ## # ## # ## #
# DATA TYPES

# Booleans
None # Nonetype is the absence of explicit value (Nonetype is falsy) -- also used a null
True # truthy value
False # falsy value

# booleans and control flow
has_bank_account = True

# if has_bank_account:
#     print('there is a bank account!')
#     print('I am in the if')
#     # 
#     # more code
#     # 
# else:
#     print('there is no bank account!')

# logical operators
# and -- &&
# or -- ||
# not/! -- !

# comparison operators (return bools)
# == -- equality
# != -- not equal
# > < >= <= --  greater than/less than

account_balance = 75

# if has_bank_account and account_balance > 99:
#     print('you\'re rich!')
# # else if uses elif keyword
# elif has_bank_account and account_balance > 50:
#     print('keep saving! one day you will be rich!')
# else:
#     print('you are broke!')

# python ternary statements
# [on true] if [boolean express] else [on false]
should_get_account = 'don\'t open an account' if has_bank_account else 'open an account'
# print(should_get_account)

# ## # ## # ## # ## #
# Text Types (strings)
my_string = "double quotes are fine"
my_other_string = 'single quotes are fine'

breakfast = 'spam eggs bacon sausage'
# # using dir() to print out all of the insstance methods of an instance of an object 
# print(dir(breakfast))
# print(breakfast.upper())
# print(breakfast.index('s'))
# # bracket notation using index
# print(breakfast[5])
# # negative values start from the back
# print(breakfast[-2])
# # in keyword returns a bool (works on all data containers)
# print('spam' in breakfast)
# if 'spam' in breakfast:
#     print('well I don\'t like spam'.upper())
# # len() find out how long a string (works on all data containers)
# print(len(breakfast))
# # string slicing (works on list data containers)
# #           [start index: end index : steps]
# # defaults: [0          : last index:     1]
# # slice out spam
# print(breakfast[0:4:1]) # returns new string of indexes 0 - 4 'spam'
# print(breakfast[:4]) # same as previous line, using default values
# # i don't like spam
# print(breakfast[5:]) # remove spam, keep the rest of the string
# print(breakfast[::3]) # keep everything and skip every other
# # negative step, iterates in reverse
# print(breakfast[::-1]) # reversal trick

# ## # ## # ## # ## #
# Numeric datatypes

# integers -- whole numbers
my_int = 10
# floats are decimals
my_float = 2.17823
print(my_int, my_float)
print(type(my_int), type(my_float), type(breakfast))
# int plus float
print(10 + 10.0) # integers are coerced into floats
# no type coersion between strings and number types
# print('10' + 10) # causes an error
print(int('10') + 10) # using classes for type conversion

int # integer class
float # floating point class
str # string class

# complex number
my_complex = 3j
print(my_complex + 10j + 10)

# math operators
# + - / * % -- arithmetic
# there is no ++ --
# += -= /= *= %=
# number ** to the power of -- exponent operator
# // forced integer division (rounds down) -- Math.floor(10 / 3.3)
my_int += 33.6
print(my_int)
print(2 ** 8)
print(10 // 3.3)