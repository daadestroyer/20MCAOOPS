
import os
try:
    while True:
        ch = int(input("enter choice \n 1-CREATE A REPLICA OF THE EXISTING FILE \n 2-TO DELETE A FILE 0-EXIT \n 3-TO PRINT ALL CONTENT OF AN EXISTING \n 4-to create a file and write content to it\n 0-EXIT"))
        if ch == 1:
            file1 = input("enter the name of the existing file")
            file2 = input(
                "enter the name of the file in which the content has to be placed")
            with open(file1, "r+") as f1, open(file2, "w+") as f2:
                for line in f1:
                    f2.write(line)
                print(" COPY SUCCESSFULL , contents of copied file are")
                print(f2.readlines())
        elif ch == 2:
            file1 = input("enter the name of the existing file")
            os.remove("hi.txt")
        elif ch == 3:
            print()
except FileNotFoundError:
    print("file name given was not found")
