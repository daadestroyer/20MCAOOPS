'''
Remove Specified Item
The remove() method removes the specified item.
'''

list = ['apple','banana','mango']
list.remove('mango')
print(list)

'''
Remove Specified Index
The pop() method removes the specified index.
If you do not specify the index, the pop() method removes the last item.
'''

lst = [1,2,3,4]
lst.pop(2)
print(lst) # [1,2,4]
lst.pop()
print(lst) # [1,2]

# The del keyword can also delete the list completely.
dellist = [1,2,3,4]
del dellist
print(dellist)

'''
Clear the List
The clear() method empties the list.
The list still remains, but it has no content.
'''

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

