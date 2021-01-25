# take a string input from user
str1 = input('Enter string 1 : ')

while (True):
    print('1. convert string toUpperCase')
    print('2. convert string toLowerCase')
    print('3. find length of string')
    print('4. reverse the string')
    print('5. concat two strings')
    print('6. get first character of string')
    print('7. get last character of string')
    print('8. check string is palindrome or not')
    print('9. sort the string')
    print('10. search word in a string')
    print('11. EXIT')
    print()
    choice = int(input('Enter choice : '))

    if choice == 1:
        print(str1.upper())
    elif choice == 2:
        print(str1.lower())
    elif choice == 3:
        print(len(str1))
    elif choice == 4:
        print(str1[::-1])
    elif choice == 5:
        str2 = input('Enter string 2 : ')
        print(str1+" "+str2)
    elif choice == 6:
        print(str1[0])
    elif choice == 7:
        print(str[-1])
    elif choice == 8:
        str2 = str1[::-1]
        if str1 == str2:
            print('Palindrome')
        else:
            print("Not Palindrome")
    elif choice == 9:
        print(sorted(str1))
    elif choice == 10:
        search = input("Enter word/character to search in a string : ")
        print(str1.find(search))
    else:
        break;

print("EXITED...")
