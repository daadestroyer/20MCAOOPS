while True:
    print('1. get first element')
    print('2. reverse list')
    print('3. remove last element')
    print('4. get last element')
    print('5. remove first element')
    print('6. sort list')
    print('7. append element')
    print('8. insert element')
    print('9. count element')
    print('10. extend set')
    print('0. EXIT')

    choice = int(input('Enter choice : '))

    if choice == 1:
        lst = list(input('enter element'))
        print(lst[0])
    elif choice == 2:
        lst = list(input('enter element'))
        print(lst[::-1])
    elif choice == 3:
        lst = list(input('enter element'))
        print(lst.pop())
    elif choice == 4:
        lst = list(input('enter element'))
        print(lst[-1])
    elif choice == 5:
        lst = list(input('enter element'))
        print(lst.remove(0))
    elif choice == 6:
        lst = list(input('enter element'))
        print(lst.sort())
    elif choice == 7:
        lst = list(input('enter element'))
        ele = input('enter element to append')
        print(lst.append)
    elif choice == 8:
        lst = list(input('enter element'))
        ele = input(('enter element'))
        print(lst.insert(2,ele))
    elif choice == 9:
        lst = list(input('enter element'))
        ele = input('enter element to count')
        print(lst.count(ele))
    elif choice == 10:
        lst1 = list(input('enter element'))
        lst2 = list(input('enter element'))
        print(lst1.extend(lst2))
    else:
        print('EXITING...')
        break
