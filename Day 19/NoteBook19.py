class A:
    def funA(self):
        print("Hello")

class B:
    def funB(self):
        print("Bye")


class C(B,A):
    def myfun(self):
        print("hi")


c =C()

c.funA()
c.funB()
c.myfun()
