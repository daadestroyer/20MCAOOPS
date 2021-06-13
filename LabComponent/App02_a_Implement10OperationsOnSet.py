while True:
		print('1. size of set')
		print('2. get length of set')
		print('3. add value to set')
		print('4. pop')
		print('5. intersection')
		print('6. set difference')
		print('7. symmetric difference')
		print('8. remove specifie element')
		print('9. clear set')
		print('10. delete set')

		choice = int(input('enter choice'))

		if choice == 1:
			st = set(input('enter element'))
			print(st.__sizeof__())

		elif choice == 2:
			st = set(input('enter element'))
			print(len(st))

		elif choice == 3:
			st = set(input('enter element'))
			st.add(1000)
			print(set)

		elif choice == 4:
			st = set(input('enter element'))
			st.pop()
			print(st)

		elif choice == 5:
			st1 = set(input('enter element'))
			st2 = set(input('enter element'))
			print(st1.intersection(st2))
			

		elif choice == 6:
			st1 = set(input('enter element'))
			st2 = set(input('enter element'))
			print(st1-st2)

		elif choice == 7:
			st1 = set(input('enter element'))
			st2 = set(input('enter element'))
			print(st1^st2)

		elif choice == 8:
			st = set(input('enter element'))
			ele = input('enter element')
			st.remove(ele)
			print(st)

		elif choice == 9:
			st = set(input('enter element'))
			st.clear()
			print(st)

		elif choice == 10:
			st = set(input('enter element'))
			del st
			print(st)

		else:
			print('')
			print('*** EXITING ***')
			break
