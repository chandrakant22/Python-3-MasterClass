# Python Constructors
# Python Constructor. A constructor is a special type of method (function) 
# which is used to initialize the instance members of the class.
# default  
# parameterized

class Student:
    roll=None
    name=None
    p1=0
    p2=0
    p3=0

    def __init__(self):
         print("hey i am const")
         self.roll=999
         self.name="not set"
         self.p1=0
         self.p2=0
         self.p3=0

    def __init__(self,roll,name,p1,p2,p3):
        self.roll=roll
        self.name=name
        self.p1=p1
        self.p2=p2
        self.p3=p3
    
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
      

    def setStudentData(self,roll,name,p1,p2,p3):
        self.roll=roll
        self.name=name
        self.p1=p1
        self.p2=p2
        self.p3=p3

    def showStudentData(self):
        print("Roll :",self.roll)
        print("Name :",self.name)
        print("Result :",self.p1 +self.p2+self.p3)




s= Student(101,"geeta",20,20,20)
s.showStudentData()

s1= Student(101,"geeta")
s1.showStudentData()


# s.setStudentData(101,"ram",10,10,10)
# s.showStudentData()


# s1=Student()
# s1.setStudentData(102,"sham",20,20,20)
# s1.showStudentData()


# s2=Student()
# s2.showStudentData()
# print(s.roll)



