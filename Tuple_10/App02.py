'''
Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:
'''

thistuple = ('apple', 'banana', 'cherry')
print(thistuple[1])

# Accessing Negative Index
print()
print(thistuple[-1])
print(thistuple[-2])

'''
Range of Indexes
you can specify the start and end of the tuple to get those elements
'''

thistuple = ('apple', 'banana', 'cherry', 'mango', 'orange', 'watermelon')
print(thistuple[2:5])  # print start from 2nd index till 4th index
print(thistuple[:4])  # print till 4th-1 index
print(thistuple[4:])  # start printing from 4th index

# Range of Negative Indexes
print(thistuple[-4:-1])  # ('cherry', 'mango', 'orange')

'''
Check if Item Exist
To determine if a specified item is present in a tuple use the in keyword:
'''

if 'cherry' in thistuple:
    print("exist")
else:
    print('not exits')
