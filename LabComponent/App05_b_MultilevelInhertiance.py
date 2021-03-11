class student:
    def __init__(self, usn, name, age):
        self.usn = usn
        self.name = name
        self.age = age

    def display(self):
        print("name: %s" % self.name)
        print("USN: %s" % self.usn)
        print("age: %d" % self.age)


class MCA(student):
    def __init__(self):
        usn = input("enter the usn number")
        name = input("enter the name")
        age = int(input("enter age"))
        student.__init__(self, usn, name, age)
        self.marks = []
        self.semester = input("Enter semester")
        for i in range(1, 6):
            self.marks.append(int(input("enter marks in subject out of 50")))

    def display(self):
        student.display(self)
        print("semester: %d" % self.age)
        for i in range(0, 5):
            print("marks in sub {}::{}".format((i+1), self.marks[i]))


class bsec(MCA):
    def __init__(self):
        MCA.__init__(self)
        self.total = 0
        self.coordinator = input("enter your coordinator")
        for i in range(0, 5):
            self.total += self.marks[i]
        self.percent = (self.total/250)*100
        MCA.display(self)
        bsec.display(self)

    def display(self):
        print("coordinator of b sec is %s" % self.coordinator)
        print("percent is %d" % self.percent)


ansh = bsec()