class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,empid,pay):
        if not first:
            print('invalid')
        else:
            self.first = first

        if not last:
            print('invalid')
        else:
            self.last = last

        if empid == 0 or empid <= 0:
            print('invalid')
        else:
            self.empid = empid

        if pay == 0 or pay <= 0:
            print('invalid')
        else:
            self.pay = pay

            
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def displayDetails(self):
        print(self.first)
        print(self.last)
        print(self.empid)
        print(self.pay)


class Developer(Employee):
    raise_amt = 1.05

    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amt)

class Manager(Employee):
    raise_amt = 1.06

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


m1 = Manager("Ravi","Shankar",1001,50000)
d1 = Developer("Shashi","Kumar",1002,60000)
m1.displayDetails()
print()
d1.displayDetails()
