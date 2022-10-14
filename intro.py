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

# define a variable (no variable declaration keyword) (they work as a 'let' -- 'const' does not exist in python)
my_variable = 'spam'
print(my_variable)
my_variable = 'eggs'
print(my_variable)
# there is no const, but convention among python programmers indicates consts WITH_CAPS
MY_CONST = 'do not change me'
# MY_CONST = 'will this work?'

# ## # ## # ## # ## #
# DATA TYPES

# Booleans
None # Nonetype is the absence of explicit value (Nonetype is falsy) -- also used a null
True # truthy value
False # falsy value

# booleans and control flow
has_bank_account = True

if has_bank_account:
    print('there is a bank account!')
    print('I am in the if')
    # 
    # more code
    # 
else:
    print('there is no bank account!')

# logical operators
# and -- &&
# or -- ||
# not/! -- !

# comparison operators (return bools)
# == -- equality
# != -- not equal
# > < >= <= --  greater than/less than

account_balance = 75

if has_bank_account and account_balance > 99:
    print('you\'re rich!')
# else if uses elif keyword
elif has_bank_account and account_balance > 50:
    print('keep saving! one day you will be rich!')
else:
    print('you are broke!')