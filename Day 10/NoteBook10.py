#Loop
#while
#for

#break
#continue




class Student:
    
    roll=0
    name=""
    p1=0.0
    p2=0.0
    p3=0.0

    def myfun(self):
        print("hello Student")


    def show(self):
        print(self.roll," ",self.name," ",self.p1+self.p2+self.p3)


s= Student()
s.myfun()
s.roll=101
print("roll ",s.roll)
