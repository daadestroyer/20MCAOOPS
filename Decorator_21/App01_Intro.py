'''
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently
modifying it.

First class functions
---------------------
First class functions are those which can be used or passed as a arguments

1. A functions is an instance of object type
2. You can store the function in a variable
3. You can pass the function as a parameter to another function
4. You can return the function from function
5. You can store them in data structures such as hash tables , lists ...
'''

'''
# Treating the function as objects
#---------------------------------
def shout(text):
    return text.upper()

print(shout("shubham"))
obj = shout("shubham")
print(obj)
'''

'''
# Passing function as a arguments
#--------------------------------
def convertUpper(text):
    return text.upper()

def convertLower(text):
    return text.lower()

def greet(func):
    res = func("shubham nigam")
    print(res)

greet(convertLower)
greet(convertUpper)
'''

'''
#=====================================================  
# Returning the function from another function
#---------------------------------------------
def createAdder(x):
    def adder(y):
        return x+y
    return adder

add_15 = createAdder(15)
print(add_15(10))
'''

'''
#=====================================================
# decorator without annotation
#-----------------------------
def dec1(func):
    def func():
        print("before execution")
        func()
        print("after execution")

def fun2():
    print("func1 executed...")

fun2 = dec1(fun2)
fun2()

#======================================================
'''

'''
# decorator with annotation
#--------------------------
def dec1(func):
    def fun():
        print("before execution")
        func()
        print("after execution")
    return fun

@dec1
def fun2():
    print("func1 executed...")

fun2()

#======================================================
'''



'''
# Returning function inside another function
#-------------------------------------------
def wrapperfun(callhello):
    def fun2(val):
        print(val)
        callhello(val)
    return fun2

@wrapperfun
def hello(val):
    print("i send the function inside wrapper")

hello(5)
'''


