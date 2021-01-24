fruits = ['banana','apple','mango','melon']
newlist = []

for x in fruits:
    newlist.append(x.upper())

print(newlist)

# sort list alphanumerically
fruits.sort()
print(fruits)

# sort list numerically
nos = [4,2,5,1,6,3]
nos.sort()
print(nos)

# sort descending order
nos.sort(reverse=True)
print(nos)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist.reverse()
print(thislist)
thislist.sort(reverse=True)
print(thislist)


# python copy list

originallist = [1,2,3,4,5]
copylist = originallist.copy()
print(copylist)
