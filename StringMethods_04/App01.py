#capitalize
txt = "shubham nigam"
print(txt.capitalize())

# capitalize
print()
txt = "banana"
print(txt.center(20))

# endsWith
print()
msg = "hello this is shubham nigam"
print(msg.endswith("nigam"))

# count
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# find
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# format
print("my name is shubham {}".format("nigam"))

# isalnum (containing both number and letter)
txt = "Company12"
x = txt.isalnum()
print(x)

# isalpha (all the characters in the text are letters)
txt = "CompanyX"
print(txt.isalpha())

# index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# isdecimal (all the characters in the unicode object are decimals)
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

# isdigit (all the characters in the text are digits)
txt = "50800"
x = txt.isdigit()
print(x)

# islower

# isnumeric
txt = "565543"
x = txt.isnumeric()
print(x)

# isupper

# isspace (all the characters in the text are whitespaces)
txt = "  "
x = txt.isspace()
print(x)

# join (Join all items in a tuple into a string, using a hash character as separator)
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# lower (convert string to lower case)
# replace (return and replace string with another string)
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# partition ()
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x) #  ('I could eat ', 'bananas', ' all day')