'''
Access Items
1. You cannot access items in a set by referring to an index or a key.
2. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in
   keyword.
3. Sets are used to store multiple items in a single variable.
4. A set is a collection which is both unordered and unindexed.
5. Note: Sets are unordered, so you cannot be sure in which order the items will appear.
6. Unordered means that the items in a set do not have a defined order
7. Sets are unchangeable, meaning that we cannot change the items after the set has been created.
8. Sets cannot have two items with the same value.
'''

# set datatypes
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# iteration in set items
print()
thisset = {"apple","banana","mango"}
for x in thisset:
    print(x)

# Check banana is present in this set or not
print()
print("banana" in thisset)

# Once set is created you can't change set items

'''
add item in set
To add one item to a set use the add() method.
'''
print()
thisset.add("cherry")
print(thisset)

# add one set into another set using update method
print()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

'''
Remove set items
To remove an item in a set, use the remove(), or the discard() method.
'''
print()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# To remove last item we can use pop()
print()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:
print()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:

# Loop
print()
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)