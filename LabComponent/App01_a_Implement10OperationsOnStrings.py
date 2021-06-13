while(True):
	print('1. convert to lower case')
	print('2. convert to upper case')
	print('3. length of string')
	print('4. reverse string')
	print('5. concat two string')
	print('6. get first character of string')
	print('7. get last character of string')
	print('8. get substring')
	print('9. repeat string twice')
	print('10. check character present in string or not')
	print('0. EXIT')
	print('')
	choice = int(input('enter your choice : '))

	if choice == 1:
		str = input('enter string : ')
		print(str.lower())
	elif choice == 2:
		str = input('enter string : ')
		print(str.upper())
	elif choice == 3:
		str = input('enter string : ')
		print(len(str))
	elif choice == 4:
		str = input('enter string : ')
		print(str[::-1])
	elif choice == 5:
		str1 = input('enter 1st string : ')
		str2 = input('enter 2nd string : ')
		print(str1+str2)
	elif choice == 6:
		str = input('enter string : ')
		print(str[0])
	elif choice == 7:
		str = input('enter string : ')
		print(str[-1])
	elif choice == 8:
		str = input('enter string : ')
		print(str[2:4])
	elif choice == 9:
		str = input('enter string : ')
		print(str*2)
	elif choice == 10:
		str = input('enter string : ')
		char = input('enter character to check : ')
		print(char in str)
	else :
		print('')
		print('*** EXITING ***')
		break
