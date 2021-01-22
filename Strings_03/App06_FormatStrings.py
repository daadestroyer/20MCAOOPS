'''
String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)

But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
'''

age = 36
txt = "my name is john, and i'm {}"
print(txt.format(age))

# or

age = 36
print("my name is john, and i'm {}".format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
item_no = 456
price = 49.5
print("i want {} pieces of item no {} for {} dollars".format(quantity,item_no,price))