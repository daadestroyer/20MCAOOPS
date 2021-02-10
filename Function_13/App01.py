def myFun(x) :
    print("Hello "+x+" !")

myFun('Shubham')


def sum(x,y):
    return x+y

print(sum(2,3))

'''
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * 
before the parameter name in the function definition.
'''

def myFun(*No):
    print(No)
    print(No[2])
myFun(1,2,3,4)


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
my_function("Emil","Tobias","Linus")


def my_function(**kid):
  print(kid)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()          # here default value which is norway will take place
my_function("Brazil")


# Passing a List as an Argument