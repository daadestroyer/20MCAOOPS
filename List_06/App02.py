'''
Change Item Value
To change the value of a specific item, refer to the index number:
'''

thislist = ['apple','banana','cherry']
thislist[1] = 'blackcurrent'
print(thislist) # ['apple', 'blackcurrent', 'cherry']

'''
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index 
numbers where you want to insert the new values:
'''
lst = ['apple','banana','cherry','orange','kiwi','mango']
thislist[1:3] = ['blackcurrent','watermelon']
print(thislist) # ['apple', 'blackcurrent', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

'''
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
'''

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)