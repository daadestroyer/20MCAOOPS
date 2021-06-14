'''
A generator function is just like a normal functin , but whenever it needs to generate a value , it does so with yield
keyword rather than return . If the body of def contains yield , the function automatically becomes a generator function

Iterable - __iter__() or __getItem__()
Iterator - __next__()
Iteration - the work of iterating on the list of values called Iteration

If i can able to iterate on some items then it is Iterable if not then it is not Iterable using __iter__() it will generate
one Iterator and in that Iterator using __next__() we can iterate


Generators are nothing but a iterators only , they are some king of iterator where we can iterate only once
Yield is use to generate values on fly not already defined value


We can't get iterable object on Int


Generator Function:
------------------
>> A generator function is defined like a normal-function , but whenever it needs to generate some values , it does so with the
   yield keyword rather than return or print statement
>> If the body of def contains yield , the function automatically becomes a generator function

Generator Object:
-------------------
>> Generator function return a generator object .
>> Generator object are used either by calling the next method on the generator object or using the generator object in a "for in"
   loop


Advantage
---------
1. we can pass generator as function arguement
2. memory saving

'''


# Simple example to generate 50 values
#-------------------------------------
def gen(n):
    for i in range(n):
        yield i


g = gen(50)
print(g) # this will print generator
for i in g:
    print(i)
#====================================

# Generator Object Example
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# x is a generator object
x = simpleGeneratorFun()
print(x.__next__())
print(x.__next__())
print(x.__next__())
