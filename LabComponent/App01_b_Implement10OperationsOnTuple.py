while (True):
    print('1. Add items in tuple and display it')
    print('2. Get first element of tuple')
    print('3. Get last element of tuple')
    print('4. Multiplication in tuple')
    print('5. Reverse tuple')
    print('6. Check item exist in tuple or not')
    print('7. Find length of tuple')
    print('8. Find max in tuple')
    print('9. Find min in tuple')
    print('10. Count particular element in tuple')
    print('11. Deleting a tuple')
    print('12. EXIT')
    choice = int(input('Enter choice : '))

    if choice == 1:
        tpl = ()
        lst = list(tpl)
        n = int(input('Enter size of tuple'))
        while n!=0:
            item = input('Enter item')
            lst.append(item)
            n-=1
        tpl = tuple(lst)
        print(tpl)

    elif choice == 2:
        print(tpl[0])
    elif choice == 3:
        print(tpl[-1])
    elif choice == 4:
        print(tpl*2)
    elif choice == 5:
        print(tpl[::-1])
    elif choice == 6:
        item = input('Enter item to search')
        print(item in tpl)
    elif choice == 7:
        print(len(tpl))
    elif choice == 8:
        print(map(tpl))
    elif choice == 9:
        print(min(tpl))
    elif choice == 10:
        item = input('Enter element to count')
        print(tpl.count(item))
    elif choice == 11:
        del tpl
    else:
        break;


print('EXITED...')