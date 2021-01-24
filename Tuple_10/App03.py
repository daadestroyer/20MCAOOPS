'''
UPDATE TUPLES
tuples are immutable / unchangeabe
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple
'''
x = ('apple', 'mango', 'orange')
y = list(x) # convert tuple to list
y[1] = 'kiwi' # make changes
x = tuple(y) # again convert list to tuple
print(x)

'''
Once tuple is created you can not add item into it , you can do this by changing tuple into list then adding item and then again
convert back to tuple
'''

tpl = (1,2,3,4)
lst = list(tpl)
lst.append("orange")
tpl = tuple(lst)
print(tpl)

'''
Removing Items , as tuple is inchangeable you can not remove item from it , but converting tuple into list and then making 
change in it after that again converting it again in tuple will work
'''

lst = list(tpl)
lst.remove("orange")
tpl = tuple(lst)
print(tpl)

# You can delte the tuple completely

del tpl
print(tpl) #this will raise an error because the tuple no longer exists

