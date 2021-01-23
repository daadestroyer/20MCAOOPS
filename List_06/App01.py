'''
1. Lists are used to store multiple items in a single variable.
2. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary,
   all with different qualities and usage.
3. Lists are created using square brackets
'''

list = ['shubham','sakshi','shubhanshu']
print(list)

# Access Items
print(list[0])

list.append('kshitij')
print(list)

list.remove('kshitij')
print(list)

list[1]='sakshi nigam'
print(list)

list.append('shubhanshu')
print(list)

print(len(list))

list1 = [1,2,3,4]
list2 = [True,False,True,False]
print(list1)
print(list2)

print(type(list))
print(type(list1))
print(type(list2))

'''
Negative Indexing
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.
'''

# print last item of list
print(list1[-1])
print(list1[-2])

'''
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
'''

lst = ["apple","banana","mango","orange","avocado","coconut"]
print(lst[2:5]) # ['mango', 'orange', 'avocado']


# return item till specified index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# return item from specified index to last

print(thislist[2:])

'''
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:
'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

'''
Check if Item Exists
To determine if a specified item is present in a list use the in keyword
'''

thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("Yes apple is present")
else :
    print("No apple is not present")