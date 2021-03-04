from magic import *

ob = magic()
ob1 = magic()

ob.__input__()
ob1.__input__()

while True:
        print("1- add \n ")
        print("2- add \n ")
        print("3- add \n ")
        print("4- add \n ")
        print("0- exit \n ")

        ch = int(input('Enter your choice : '))
        if ch == 1:
            ob+ob1
        elif ch==2:
            ob-ob1
        elif ch==3:
            ob*ob1
        elif ch==4:
            ob/ob1
        else:
            break
