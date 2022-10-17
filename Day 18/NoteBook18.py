class Person:
    def __init__(self):
        self.name=""
        self.address=""
        self.mobile=""
    
    def setData(self):
        self.name=input("Enter your name ")
        self.address=input("Enter your Address ")
        self.mobile=input("Enter your mobile number ")
    
    def show(self):
        print("Your name :",self.name)
        print("Your address :",self.address)
        print("Your mobile :",self.mobile)

class Student(Person):
    def __init__(self):
        self.roll=""
    
    def setStudentData(self):
        print("Enter Data for Student")
        self.roll=input("Enter your roll ")
        Person.setData(self)

    def showStudent(self):
        print("Roll :",self.roll)
        Person.show(self)

class Emp(Person):
    def __init__(self):
         self.empID=""

    def setEmpData(self):
        print("Enter Data for Emp")
        self.empID=input("Enter your EmpID ")
        Person.setData(self)

    def showEmp(self):
        print("Roll :",self.empID)
        Person.show(self)


s=Student()
s.setStudentData() #roll
#s.setData() #name address mobile       

s.showStudent()
#s.show()

e=Emp()
e.setEmpData() #roll
#s.setData() #name address mobile       

e.showEmp()


# p=Person()
# p.setData()
# p.show()

