import math


# lambda function for power
lam = lambda x : math.pow(x,x)
print(math.floor(lam(2)))

# lambda function to concat string
lam = lambda s : s+s
print(lam('shubham'))

# write a lambda function to join list
lam = lambda x,y : x+y
print(lam([1,2,3],[4,5,6]))

# add two list without using lambda function
def add(a,b):
    return a+b
lst1 = [1,2,3]
lst2 = [4,5,6]

lst3 = map(add(lst1,lst2),lst1,lst1)
print(lst3)

# add two list elements with using lambda function
lam = map(lambda x,y:x+y,[1,2,3],[4,5,6])
print(list(lam))
