# If statement:

a = 66
b = 44
if a > b:
    print("{}".format(a) + " is greater than {}".format(b))
else:
    print("{}".format(a) + " is less than {}".format(b))

# Elif

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short Hand If ... Else
a = 2000
b = 2000
print("A") if a > b else print("B")

print("A") if a > b else print("A==B") if a == b else print("B")


# And
# The and keyword is a logical operator, and is used to combine conditional statements:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

'''
Or
The or keyword is a logical operator, and is used to combine conditional statements:
'''

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

'''
Nested If
You can have if statements inside if statements, this is called nested if statements
'''

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")