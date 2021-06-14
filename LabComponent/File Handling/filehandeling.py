import os
while True:
            print('1. FileNotFound Error')
            print('2. TypeError')
            print('3. IOError')
            print('4. FileExistError')
            print('5. AtributeError')
            print('6. EXIT')    
            print()
            ch = int(input('Enter your choice : '))

            if ch == 1:
                    try:
                        # if file will not exist FileNotFoundError will come
                        f = open('sdss.txt','r')
                        print()
                        print("=====SUCCESSFULLY=====")
                        print()
                    except FileNotFoundError:
                        print()
                        print("======FileNotFoundError======")
                        print()

            elif ch == 2:
                    try:
                        # Giving extra mode like 'a' then TypeError will come , if we remove 'a' it will work fine
                        f = open('abc.txt','w','a')
                        print()
                        print("=====SUCCESSFULLY=====")
                        print()
                    except TypeError:
                        print()
                        print("======TypeError======")
                        print()
            
            elif ch == 3:
                    try:
                        # open a file or create it using w+ mode
                        f = open('abc.txt','w+')
                        f.write('sample content')
                        # we created abc.txt but we're opening  cccc.txt file then IOError will come
                        f1 = open('cccc.txt','r')
                        print()
                        print()
                        print("=====SUCCESSFULLY=====")
                    except IOError:
                        print()
                        print("======IOError======")
                        print()
            
            elif ch == 4:
                    try:
                        # if file is not exist then it will give FileExistError
                        f = os.path.exists('123.txt')
                        print(f)
                        if f == False :
                            raise FileExistsError

                        print()
                        print("=====SUCCESSFULLY=====")
                        print()
                    except FileExistsError:
                        print()
                        print("======FileExistError======")
                        print()

            elif ch == 5:
                    try:
                        # we open file in append mode
                        f = open('abc.txt','a')
                        # again we open file in read mode
                        f.open('abc.txt','r')
                        print()
                        print("=====SUCCESSFULLY=====")
                        print()
                    except AttributeError:
                        print()
                        print("======AttributeError======")
                        print()
                    
            elif ch == 6:
                        print('**************************')
                        print('\t EXITING')
                        print('**************************')
                        break
            else:
                        print("=====Invalid Input Please Try Again=====")
