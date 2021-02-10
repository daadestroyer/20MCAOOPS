# Filter the array, and return a new array with only the values equal to or above 18:
ages = [5, 12, 17, 18, 24, 32]
res = list(filter(lambda ages : ages >=18,ages))
print(res)

# filter all no which are divisible by 2
no = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda  no : no % 2 == 0,no))
print(res)

# take a list of string and filter all string whoose length is less than 5
names = ['sakshi','shubham','shubhanshu','raj','aman','vinay','ajay']
list = list(filter(lambda names : len(names)>5,names))
print(list)