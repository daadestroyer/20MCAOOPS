while True:
    print('1. concat tuple :')
    print('2. find max :')
    print('3. find min :')
    print('4. reverse tuple :')

    choice = int(input('enter choice'))

    if choice == 1:
        t1 = tuple(input('enter tuple 1'))
        t2 = tuple(input('enter tuple2'))
        print(t1+t2)

    elif choice == 2:
        t1 = tuple(input('enter tuple'))
        print(max(t1))

    elif choice == 3:
        t1 = tuple(input('enter tuple'))
        print(min(t1))

    elif choice == 4:
        t1 = tuple(input('enter tuple'))
        print(t1[::-1])

    else:
        print('exiting')
        break