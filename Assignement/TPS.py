d = dict()
msg = ""
class Student:

    def takeInput(self):
        try:
            NAME = input("enter student name : ")
            if len(NAME) == 0 :
                msg = "***** EXCEPTION : Sorry name name is necessary *****"
                raise Exception()
            else:
                self.name = NAME

            USN = input("enter student usn :")

            if len(USN) == 0 :
                msg = "***** EXCEPTION : Sorry USN is necessary *****"
                raise Exception()
            elif len(USN) > 12 or len(USN) < 12:
                msg = "***** EXCEPTION : Sorry USN can't be less/more than 11 *****"
                raise Exception()
            else:
                self.usn = USN

            MFCA = int(input("enter mfca marks :"))
            if MFCA < 0:
                msg = "***** EXCEPTION : Sorry marks can not be negative *****"
                raise Exception()
            else:
                self.mfca = MFCA

            CN = int(input("enter cn marks :"))
            if CN < 0:
                msg = "***** EXCEPTION : Sorry marks can not be negative *****"
                raise Exception()
            else:
                self.cn = CN

            LSS = int(input("enter lss marks :"))
            if LSS < 0:
                msg = "***** EXCEPTION : Sorry marks can not be zero *****"
                raise Exception()
            else:
                self.lss = LSS

            OOPS  = int(input("enter oops marks :"))
            if OOPS < 0:
                msg = "***** EXCEPTION : Sorry marks can not be zero *****"
                raise Exception()
            else:
                self.oops = OOPS


            WEB = int(input("enter web marks :"))
            if WEB < 0:
                msg = "***** EXCEPTION : Sorry marks can not be zero *****"
                raise Exception()
            else:
                self.web = WEB

            self.avg = int((self.mfca+self.cn+self.lss+self.oops+self.web)/500*100)
            self.addEmployee()
        except:
                print("=====================================================")
                print(msg)
                print("=====================================================")


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
