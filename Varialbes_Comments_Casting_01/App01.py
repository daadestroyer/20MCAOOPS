"""
x = 5
y = 'a'
z = "shubham"
print(x) # x = 5
print(y) # y = a
print(z) # z = shubham
"""

"""
x = str(3)         # x will be '3'
y = int(3)         # y will be 3
z = float(3)       # z will be 3.0
print(x)
print(y)
print(z)
"""

"""
p = 5
y = "john"
print(type(p))
print(type(y))
"""

"""
x,y,z = "Orange","Banana","Apple"
x1 = y1 = z1 = "Orange"
print(x)
print(y)
print(z)
print("")
print(x1)
print(y1)
print(z1)
"""

"""
fruits = ["apple","banana","mango"]
x,y,z = fruits
print(x)
print(y)
print(z)
"""

"""
x = "awesome"
print("python is :"+x)

x = int(input("enter no 1"))
y = int(input("enter no 2"))
print(x+y)
"""


# GLOBAL VARIABLES
x = "awesome"
def testing():
    print("python is : "+x)
testing()


# LOCAL VARIABLES
x = "cool"
def test():
    x = "fantastic"
    print("python is "+x)
test()
print("python is "+x)

# THE GLOBAL KEYWORD
def myFun():
    global x
    x = "fantastic"
myFun()
print("python is "+x)

# CHANGE GLOBAL KEYWORD
x = "wow"
def fun():
    global x
    x = "ek no.."
fun()
print("python is "+x)
