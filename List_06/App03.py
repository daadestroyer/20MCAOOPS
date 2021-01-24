'''
Append Items
To add an item to the end of the list, use the append() method:
'''

lst = ['apple','banana','cherry']
lst.append('mango')
print(lst) # ['apple', 'banana', 'cherry', 'mango']

'''
Insert Items
To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:
'''

lst.insert(2,'watermelon')
print(lst) # ['apple','banana','watermelon','cherry']

'''
Extend List
To add all the item of one list to another list use extend() 
'''

lst1 = [1,2,3,4]
lst2 = [5,6,7,8]

lst1.extend(lst2)
print(lst1) # [1, 2, 3, 4, 5, 6, 7, 8]

'''
Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
'''

list1 = ['apple','banana','mango']
tuple1 = ('kiwi','watermelon')
list1.extend(tuple1)
print(list1)