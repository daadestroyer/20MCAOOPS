'''
ORDERED
Tuple are ordered , means that item have defined order , and that order will not change

UNCHANGEABLE
Tuples are unchangeable , meaning that we cannot change , add or remove items after the tuple is created, while list are
changeable

ALLOW DUPLICATES
Tuple allow duplicates values as well , similarly List also allowed duplicate value also
'''

thistuple = ('apple','mango','orange','apple')
print(thistuple)

print(len(thistuple))

'''
Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
'''
thistuple = ('apple',)
print(type(thistuple)) # its a tuple

thistuple = ('apple')
print(type(thistuple))

'''
Tuple Items - Data Types
Tuple items can be of any data type:
'''
print()

tuple1 = ('apple','banana','cherry')
tuple2 = (1,2,3,4,5,6)
tuple3 = (True,False,False)

print(tuple1)
print(tuple2)
print(tuple3)

# A tuple with strings, integers and boolean values
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)