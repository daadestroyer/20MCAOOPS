while (True):
    print('1. Extract element from tuple')
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
    		t = tuple(input('enter element'))
    		c = int(input('enter location'))
    		if c > len(t):
    			print('wrong input location')
    		else:	
    			print(t)
    			print(t[c])
    elif choice == 2:
        t = tuple(input('enter element'))
        print(t[0])
    elif choice == 3:
        t = tuple(input('enter element'))
        print(t[-1])
    elif choice == 4:
    		t = tuple(input('enter element'))
    		print(t*2)
    elif choice == 5:
    		t = tuple(input('enter element'))
    		print(t[::-1])
    elif choice == 6:
    		t = tuple(input('enter element'))
    		item = input('enter item')
    		print(t.index(item))
    		    
    				
