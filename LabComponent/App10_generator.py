import time


def timeit(func):

    def timed(*args, **kw):
        starttime = time.time()
        result = func(*args, *kw)
        endtime = time.time()
        print("time taken", endtime-starttime)
        return result
    return timed


@timeit
def fib(a=0, b=1):
    while True:
        yield a
        a, b = b, a+b


f = fib()
num = int(input("enter range for series"))
for i in range(num):
    print(next(f))
    
    

# def fib(limit):	
# 	a, b = 0, 1

# 	while a < limit:
# 		yield a
# 		a,b=b,a+b

# x = fib(5)

# # try:
# #     while True:
# #         print(x.__next__())
# # except StopIteration:
# #     print('STOP ITERATING')
    
# for i in x:
#     print(i)



