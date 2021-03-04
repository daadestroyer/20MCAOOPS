from magic import *
ob = magic()
ob1 = magic()
ob.input()
ob1.input()


while True:
    print("1- add \n")
    print("2- sub \n ")
    print("3- mul \n ")
    print("4- div \n ")
    print("0-  exit")
    ch = int(input("enter your choice"))
    if ch == 1:
        ob+ob1
    elif ch == 2:
        ob-ob1
    elif ch == 3:
        ob*ob1
    elif ch == 4:
        ob/ob1
    elif ch == 0:
        break
    else:
        break