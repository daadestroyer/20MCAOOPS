thisset = {"apple", "banana", "cherry"}
thisset.clear()
n = int(input('enter size'))
while n != 0:
    ele = input('enter element')
    thisset.add(ele)
    n -= 1
ser = input('enter ser')
print(ser in thisset)
