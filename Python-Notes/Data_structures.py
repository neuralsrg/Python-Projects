# todo LIST

# Since we can add and remove items, we say that a list is a
# mutable data type i.e. this type can be altered.

# mylist = [1, 2, 3, [4, 5, 6]]
# help(list) to learn about some list features

print('\n\n LISTS')
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

# todo TUPLE

# Tuples are used to hold together multiple objects
# One major feature of tuples is that they are immutable like strings i.e. you cannot modify tuples.

print('\n\n TUPLES')
zoo = ('python', 'elephant', 'penguin')
new_zoo = 'monkey', 'camel', zoo

# All the same METHODS except methods which change the list itself. I. e. there is no __iadd__ here as it changes
# the current list. But it's possible to use __add__ with TUPLE as it creates the new list / tuple

# We have to specify a single item tuple using comma after the first (and the only) item:
# singleton = (2, )


# todo DICTIONARY

# keys (name) with values (details)
# You can use only immutable objects (like strings) for the keys of a dictionary but you can use either immutable or
# mutable objects for the values of the dictionary
# This basically translates to say that you should use only simple objects for keys.

print('\n\n DICTIONARIES')
# d = {key1 : value1, key2 : value2 }
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    # items() returns a list of tuples
    # where each tuple contains a pair of items - the key followed by the value
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

# todo SEQUENCES

print('\n\n SEQUENCES')
# The major features are membership tests, (i.e. the in and not in expressions) and indexing operations

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# You can also provide a third argument for the slice, which is the step for the slicing
# (by default, the step size is 1):

shoplist = ['apple', 'mango', 'carrot', 'banana']
s = shoplist[::1]  # ['apple', 'mango', 'carrot', 'banana']
s = shoplist[::2]  # ['apple', 'carrot']
s = shoplist[::3]  # ['apple', 'banana']
s = shoplist[::-1]  # ['banana', 'carrot', 'mango', 'apple']

# todo SETS

print('\n\n SETS')
bri = set(['brazil', 'russia', 'india'])  # {'brazil', 'russia', 'india'}
if 'india' in bri:  # True
    pass
if 'usa' in bri:  # False
    pass
bric = bri.copy()
bric.add('china')
if bric.issuperset(bri):  # True
    pass
bri.remove('russia')
new_bri = bri & bric  # OR bri.intersection(bric)  {'brazil', 'india'}

# todo REFERENCES

print('\n\n REFERENCES')

# When you create an object and assign it to a variable, the variable only refers
# to the object and does not represent the object itself!
# That is, the variable name points to that part of your computer's memory where
# the object is stored. This is called binding the name to the object

shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist  # mylist is just another name pointing to the same object!
mylist = shoplist[:]  # Make a copy by doing a full slice
# mylist = shoplist.copy()


# if you want to make a copy of a list or such kinds of sequences or complex objects (not simple objects
# such as integers), then you have to use the slicing operation to make a copy


# todo More about STRINGS

print('\n\n STRINGS')
# This is a string object
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:  # The find method is used to locate the position of the given substring
                            # within the string; find returns -1 if it is unsuccessful in finding the substring
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

# Python code to convert string to list character-wise
def convert(string):
    list1 = []
    list1[:0] = string
    return list1