'''
A lambda function is a small anonymous function.
A Lambda function can take any number of arguments, but can only have one expression.
Syntax
------
lambda arguments : expression
'''

# lambda expression to add two no
lam = lambda a : a+10 # (a,b) -> a+b;
print(lam(5))


# lambda expression to multiply two no
lam = lambda  a,b : a*b
print(lam(2,3))

'''
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
'''


def myFun(n):
    return lambda a : a*n

mydoubler = myFun(2)
print(mydoubler(11))

