class operator():
    def hello(self,name,age):
        self.name=name
        self.age=age
        if (not self.age):
            print("hello",self.name)
        elif not(self.name and self.age):
            print("hello")
        else:
            print("hello",self.name)
            print("your age is",self.age)


o=operator()
while(True):
    print("eneter 1 to display age and name")
    print("eneter 2 to display name")
    print("eneter 3 to display only hello")
    ch=int(input("Ente rthe choice: "))
    if(ch==1):
        name=input("enetr your name")
        age=int(input("enter your age"))
        o.hello(name,age)
    elif(ch==2):
        name = input("enetr your name")
        age =""
        o.hello(name, age)
    elif(ch==3):
        name =""
        age =""
        o.hello(name, age)
    else:
        print("invald choice")
        break