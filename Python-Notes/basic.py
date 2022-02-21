# todo Numbers
# 2 types: integers and floats
i = 12
i = 12.3E-4  # E = 10 in the power of

# todo Strings
# Single quotes
s = 'Hello World ' \
    'Hello again'
# Double quotes
s = "What's your name?"
s = "What's your" \
    "name?"
# Triple quotes (""" or ''')
s = """What's
your
name?"""
# Strings Are Immutable (once you have created a string, you cannot change it)

# format
name = 'Serge'
age = 19
s = 'Is {0} {1}?'.format(name, age)
s = 'Is {param1} {param2}?'.format(param1=name, param2=age)
s = 'Is {0} {1}?'
s = 'Is {} {}?'  # Numbers are optional here

# Python 3.6 has "f-strings"
print(f"{name} likes Python!")  # variable name

# Precisions
print('{0:.4f}'.format(1 / 3))  # 0 is the first param
num = 1 / 3
print(f'{num:.4}')  # using variable num (f after 4 is optional here)
print('{name:_^11}'.format(name='Serge'))  # ___Serge___

# Escape Sequences
print('What\'s your name?')  # We specify the single quote as \'
print("It\"s Serge")  # We specify the double quote as \"
print('This is the first line\nAnd this is the second')  # New Line
print('tab\ttab\ttab')  # \t = tab

print(r'Newlines are indicated by \n construction')  # row string
print('Newlines are indicated by \\n construction')

# todo print
print('My name is ', end='')  # by default: end='\n'
print('Serge')  # My name is Serge

# todo operators
# // div, % mod, ** in power of
# << left shift (2 << 2 equals 8. Shifts the bits of the number to the left by the number of bits specified)
# >> right shift
# & bit-wise AND, | OR, ^ XOR, ~ invert
# == equal to, != not equal to, not [boolean]


# todo loops
# The for loop
# for i in range(..)
# range(5) -> [0, 1, 2, 3, 4]
# range(1, 5) -> [1, 2, 3, 4]
# range(1, 5, 2) -> [1, 3]
# the else part after for is additional


# todo functions
# def f1(a, b):
    # pass
    # we use 'pass' to keep the function block empty

gm = 'Good morning!'
def f1(a, b):  # a, b here are called parameters
    global gm
    gm = 'Good evening!'  # Changing GLOBAL variable gm
    # function block

f1(1, 3)  # 1, 3 here are called arguments
# When you declare variables inside a function definition, they are not related in any way to other variables with the same names
# used outside the function - i.e. variable names are local to the function. This is called the scope of the variable

# Default Argument Values

def say(message, times=1):
    print(message * times)
say('hello')
say('hello', 5)

# Keyword Parameters
def func(a, b=5, c=25):
    print(f'a is {a}, b is {b}, c is {c}')
func(15, c=45)
func(b=17, a=67)

# VarArgs Parameters

def total(a=5, *numbers, **phonebook):
    print(f'a is {a}')

    # iterate through all the items in TUPLE
    for single_item in numbers:
        print(f'single_item {single_item}')

    # iterate through all the items in DICTIONARY
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

# The RETURN statement

def maximum(x, y):
    if x >= y:
        return '{} is maximum'.format(x)
    return '{} is maximum'.format(y)
    # return = return None None is a special type in Python that represents
    # nothingness. For example, it is used to indicate that a variable has no value if it has a value of None.
print(maximum(4, 5))

def some_function():
    pass
print(some_function())  # None

# Documentation Strings

def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # The convention followed for a docstring is a multi-line string where the first line starts with a capital letter and ends with a dot.
    # Then the second line is blank followed by any detailed explanation starting from the third line.
    # convert to integers, if possible
    x = int(x)
    y = int(y)
    if x >= y:
        print('x is maximum')
    else:
        print('y is maximum')
print_max(3, 5)
print(print_max.__doc__)
# help(print_max)  # Remember to press the q key to exit help
# help()  # q to exit help

# dir() returns the list of names defined by an object. dir(sys)
# vars() returns the attributes and their values: {'__name__': '__main__', '__doc__': ' Hey there...}
# del a deletes variable a as if it never existed before


# todo Modules
# SYS
# sys.path # path to python files, including library directories
# sys.argv # arguments, parameters in the Run/Debug Configuration
# while running python file in command line, type "python run.py we are the new arguments" and "we are the new arguments" -> argv
# argv[0] = basics.py

# OS
# os.getcwd() ->  current directory of your program
# os.sep  # os.sep variable - this gives the directory separator according to your operating system, i.e. it will be '/'
# in GNU/Linux, Unix, macOS, and will be '\\' in Windows
# os.path.exists(path) returns Boolean
# os.mkdir(target_dir) makes directory
# os.system(command)  runs the command as if it was run from the system i.e. in
# the shell - it returns 0 if the command was successfully, else it returns an error number.
# We can also run any python program using os.system(command)
# os.path.exists(PATH) checks whether PATH exists

# time
# time.strftime('%Y%m%d%H%M%S') The %Y specification
# will be replaced by the year with the century and so on

# __name__
# Every Python module has its __name__ defined. If this is '__main__' , that implies that the module is being run standalone by
# the user and we can take appropriate actions. This is handy for the particular
# purpose of figuring out whether the module is being run standalone or being imported
# if __name__ == '__module1__':
#   print('This program is being run by itself')

# from..import
# from mymodule import say_hi, __version__ (here can be functions, variables etc.)
# from..import * This will import all public names but would not import __version__ because it starts with double underscores.


# todo Methods
# A class can also have methods i.e. functions defined for use with respect to that class ONLY
# mylist.append('Hey!')

# Fields are variables defined for use with respect to that class only
# mylist.field


# todo Files
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()
# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
    # close the file
f.close()



# Pickle - to store any plain Python object in a file and then get it
# back later (storing the object persistently)

import pickle
# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()
# Destroy the shoplist variable
del shoplist
# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
f.close()


# encoding=utf-8
import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)


# todo Exceptions

try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:  # Ctrl + C in console
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))


