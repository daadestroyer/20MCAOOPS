# fibonacci series using generator
import time
def timeit(func):
        def timed(*args , **kw):
                starttime = time.time()
                result = func(a , b)
                endtime = time.time()
                print("time taken", endtime-starttime)
                return result
        return timed

@timeit
def fib(a=1,b=1):
        while True:
                yield a
                a = b
                b = a + b
f = fib()
num = int(input('enter a no'))
for i in range(num):
        print(next(f))
