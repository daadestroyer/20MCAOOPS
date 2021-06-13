d = dict()
class employee:
		def input(self):
			self.name = input('enter name : ')
			self.addr = input('enter addr : ')
			self.pan = input('enter pan : ')
			self.basic = int(input('enter basic : '))
			self.tds = int(input('enter tds : '))
			self.deduct = int(input('enter decuct : '))
			self.hra = 1.25*self.basic
			self.da = 0.25*self.basic
			self.grosssal = self.basic + self.hra + self.da
			self.netpay = self.grosssal-self.deduct
			self.addemp()

		def addemp(self):
			d.update({
					self.name:{
							"name":self.name,
							"addr":self.addr,
							"pan":self.pan,
							"basic":self.basic,
							"tds":self.tds,
							"deduct":self.deduct,
							"hra":self.hra,
							"da":self.da,
							"grosssal":self.grosssal,
							"netpay":self.netpay
						}
				})

		def printallemp(self):
			for key in d:
				print(key,d[key])

		def search(self,name):
			flag = 0
			for key in d:
				if name == key:
					print('employee found')
					for i in d[key]:
						print(i,d[key][i])
						flag = 1
				if flag == 0:
					print('no record found')

class operation:
	emp = employee()

	while True:
		print('1. to add employee or employees : ')
		print('2. print all employees : ')
		print('3.find an employee by name : ')
		choice = int(input('enter choice : '))

		if choice == 1:
			emp.input()
		elif choice == 2:
			emp.printallemp()
		elif choice == 3:
			name = input('enter employee name : ')
			emp.search(name)
		else:
			print('*** EXITING ***')
