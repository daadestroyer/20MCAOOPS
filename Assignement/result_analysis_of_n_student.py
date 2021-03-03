d = dict()

class Student:

    def takeInput(self):
        self.name = input("enter student name : ")
        self.usn = int(input("enter student usn :"))
        self.mfca = int(input("enter mfca marks :"))
        self.cn = int(input("enter cn marks :"))
        self.lss = int(input("enter lss marks :"))
        self.oops = int(input("enter oops marks :"))
        self.web = int(input("enter web marks :"))
        self.avg = int((self.mfca+self.cn+self.lss+self.oops+self.web)/500*100)
        self.addEmployee()

    def addEmployee(self):
        d.update(
            {
                self.name:
                    {
                        "name":self.name,
                        "usn":self.usn,
                        "cn":self.cn,
                        "lss":self.oops,
                        "web":self.web,
                        "avg":self.avg
                    }
            }
        )

    def printAllStudent(self):

        for key in d:
            print(key, d[key])

    def printStudentDataByName(self,name):
        flag = 0
        for key in d:
            if key == name:
                print("Student Found...\n")
                for i in d[key]:
                    print(i,d[key][i])
                    flag = 1
        if flag == 0:
            print("No Student Found Of This Name : "+self.name)

class Operations(Student):
    st = Student()
    while True:
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t*************WELCOME TO STUDENT RESULT SYSTEM *************')
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*******RV COLLEGE OF ENGINEERING*******')
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t****20MCA00PS OBJECT ORIENTED PROGRAMMING****')
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t****TEAM SHUBHAM****')
        print('1. Add Student Data')
        print('2. Get All Student Data')
        print('3. Get Student Data By Name')
        print('0. EXIT')
        ch = int(input('Enter your choice'))
        if ch == 1:
            st.takeInput()
        elif ch == 2:
            st.printAllStudent()
        elif ch == 3:
            name = input("enter the name of the student to be searched")
            st.printStudentDataByName(name)
        else:
            break
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t*************THANK YOU FOR VISITING SEE YOU AGAIN *************")
