fruits = ['banana', 'apple', 'mango', 'melon']
newlist = []

for x in fruits:
    newlist.append(x.upper())

print(newlist)

# sort list alphanumerically
fruits.sort()
print(fruits)

# sort list numerically
nos = [4, 2, 5, 1, 6, 3]
nos.sort()
print(nos)

# sort descending order
nos.sort(reverse=True)
print(nos)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

thislist.reverse()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

# python copy list

originallist = [1, 2, 3, 4, 5]
copylist = originallist.copy()
print(copylist)

# python join list
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# another way to join list

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

for x in lst2:
    lst1.append(x)
print(lst1)

# use extend method to add list1 item in another list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# count
print(list1.count("a"))

# index
fruits = ['apple', 'banana', 'cherry']
print(fruits.index("cherry"))
