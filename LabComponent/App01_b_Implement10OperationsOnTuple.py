while True:
		print('1. Get first element of tuple')
		print('2. Get last element of tuple')
		print('3. reverse tuple')
		print('4. extract element from tuple')
		print('5. find length of tuple')
		print('6. get max')
		print('7. get min')
		print('8. count occurences in tuple')
		print('9. join two tuple')
		print('10. mulitply tuple by 2')
		print('')

		choice = int(input('Enter choice : '))

		if choice == 1:
			t = tuple(input('enter element : '))
			print(t[0])
		elif choice == 2:
			t = tuple(input('enter element : '))
			print(t[-1])
		elif choice == 3:
			t = tuple(input('enter element : '))
			print(t[::-1])
		elif choice == 4:
			t = tuple(input('enter element : '))
			print(t[2])
		elif choice == 5:
			t = tuple(input('enter element : '))
			print(len(t))
		elif choice == 6:
			t = tuple(input('enter element : '))
			print(max(t))
		elif choice == 7:
			t = tuple(input('enter element : '))
			print(min(t))
		elif choice == 8:
			t = tuple(input('enter element : '))
			ele = input('enter element to count : ')
			print(t.count(ele))
		elif choice == 9:
			t1 = tuple(input('enter t1 element : '))
			t2 = tuple(input('enter t2 element : '))
			print(t1+t2)
		elif choice == 10:
			t = tuple(input('enter element : '))
			print(t1*2)
		else:
			print('***EXITING***')
			break
