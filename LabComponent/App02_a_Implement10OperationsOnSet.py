while (True):
    print('1. Add item into set : ')
    print('2. Get length of set : ')
    print('3. Reverse set :')
    print('4. Remove element from set : ')
    print('5. Add one set into another set : ')
    print('6. Discard element from set : ')
    print('7. Join two sets : ')
    print('8. Get copy of set : ')
    print('9. Find element in set :')
    print('10. Remove last element from set : ')
    print('11. Clear set : ')
    print('12. Delete set : ')
    print('13. EXIT : ')
    set = {'1'}
    choice = int(input('Enter choice : '))

    if choice == 1:
        set.clear()
        item = int(input('Enter size of set'))
        while item != 0:
            n = input('Enter item')
            set.add(n)
            item -= 1
        print(set)

    elif choice == 2:
        print(len(set))



    elif choice == 6:
        print()
    elif choice == 7:
        print()

    elif choice == 9:
        ele = input('Enter element to find in set')
        print("dfdfdfdfdfdfdf "+ele in set)
    elif choice == 10:
        print("Last element of set is : "+set.pop())
    elif choice == 11:
        set.clear()
        print(set)
    elif choice == 12:
        del set
    else:
        break

print("EXITED...")
