import os

while True:
    print("1.Check File Not Found Error")
    print("2.Check Type Error")
    print("3.Check IOError")
    print("4.Check File Exist Error")
    print("5.Attribute error")
    print("6.Exit")
    n = int(input("Enter Choice:"))

    if n == 1:
        try:
            # whenever abc.txt will not there then it will FileNotFoundError
            f = open('abc.txt', 'r')
            print("Successfully")
        except FileNotFoundError:
            print()
            print("======File Not Found error======")
            print()
    elif n == 2:
        try:
            # when i will give one parameter w then it will print Successfully else TypeError will come
            f = open('abc.txt', 'w','a')
            print()
            print("======Successfully======")
            print()
        except TypeError:
            print()
            print("======Type Error======")
            print()
    elif n == 3:
        try:
            # open a file and if doesn't exist it create it
            f = open('abc.txt', 'w+')
            f.write("Sample")
            # when i will replace cc.txt to abc.txt then it will print Successfully
            f1 = open('cc.txt', 'r')
            print()
            print("======Successfully======")
            print()
        except IOError:
            print()
            print("======IO Error======")
            print()
    elif n == 4:
        try:
            # if file abc4.txt is exists then it will raise FileExistsError
            f = os.path.exists('sdsds.txt')
            print(f)
            if f == "False" :
                raise FileExistsError

            print()
            print("======Successfully======")
            print()
        except FileExistsError:
            print()
            print("======File Exist Error======")
    elif n == 5:
            try:
                f = open('abc.txt', 'a')
                # When i will comment this line it will be show AttributeError
                f.open('abc.txt', 'r')
                print()
                print("======Successful======")
                print()
            except AttributeError:
                print()
                print("======AttributeError======")
                print()
    elif n == 6:
        break
    else:
        print()
        print("======Invalid input Please try again======")
        print()
