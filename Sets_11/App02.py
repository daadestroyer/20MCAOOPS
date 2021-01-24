'''
1. Join Two Sets
2. There are several ways to join two or more sets in Python.
3. You can use the union() method that returns a new set containing all items from both sets, or the update() method that
   inserts all the items from one set into another:
'''

set1 = {'a','b','c'}
set2 = {1,2,3}
set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

# setCopy()
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# discard()
print()
fruits.discard("banana")
print(fruits)