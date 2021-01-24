'''
Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple
'''

fruits = ('apple','mango','cherry')
(green,yellow,red)= fruits
print(green)
print(yellow)
print(red)

print("green is {}".format(green)+" yellow is {}".format(yellow)+" red is {}".format(red))



'''
Using Asterix*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be
assigned to the variable as a list:
'''
print()
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

print()
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)