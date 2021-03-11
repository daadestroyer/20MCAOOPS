class STUDENT:
    def __init__(self,USN,NAME,AGE):
        self.USN = USN
        self.NAME = NAME
        self.AGE = AGE

    def display(self):
        print(self.USN)
        print(self.NAME)
        print(self.AGE)

class UGSTUDENT(STUDENT):

    def __init__(self):
        USN = input('Enter USN : ')
        NAME = input('Enter NAME : ')
        AGE = input('Enter AGE : ')
        self.SEMESTER = input('Enter SEMESTER : ')
        self.FEES = input('Enter FEES : ')
        STUDENT.__init__(self,USN,NAME,AGE)
        STUDENT.display(self)
        UGSTUDENT.display(self)

    def display(self):
        print(self.SEMESTER)
        print(self.FEES)


class PGSTUDENT(STUDENT):

    def __init__(self):
        USN = input('Enter USN : ')
        NAME = input('Enter NAME : ')
        AGE = input('Enter AGE : ')
        self.SEMESTER = input('Enter SEMESTER : ')
        self.FEES = input('Enter FEES : ')
        STUDENT.__init__(self,USN,NAME,AGE)
        STUDENT.display(self)
        PGSTUDENT.display(self)

    def display(self):
        print(self.SEMESTER)
        print(self.FEES)

while True:

        print('1. UG Student Press 1 : ')
        print('2. PG Student Press 2 : ')
        print('0. EXIT ')
        ch = int(input('Enter choice : '))

        if ch == 1:
            UG = UGSTUDENT()
        elif ch == 2:
            PG = PGSTUDENT()
        elif ch == 0 :
            print('EXITING...')
            break
        else:
            print('INVALID Choice : ')





