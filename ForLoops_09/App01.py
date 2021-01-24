'''
Python For Loops
1. A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
2. This is less like the for keyword in other programming languages, and works more like an iterator method as found in other
   object-orientated programming languages.
3. With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''

# Looping through list
fruits = ['apple','banana','mango']
for x in fruits:
    print(x)

# Looping through string
print()
for x in "banana":
    print(x)

# The break Statement
print()
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement
print()
for x in fruits:
    if x == "banana":
        continue
    print(x)

'''
1. The range() Function
2. To loop through a set of code a specified number of times, we can use the range() function,
3. The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at 
   a specified number.
'''
print()

for x in range(6): # for(int i=0 ; i<6 ; i++
  print(x)

# for loop using start and end parameter
print()
for x in range(2,6):
    print(x)

# for loop with increment sequence
print()
for x in range(2,30,3): # for(int i=2 ; i<30 ; i+=3
    print(x)

# nested for loop
print()
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)