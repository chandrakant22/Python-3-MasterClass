#Poly morphism


class Bank:
    def rateofIntrest(self):
        print("9%")

class SBI(Bank):
    def rateofIntrest(self):
        print("8%")

class IDBI(Bank):
    def rateofIntrest(self):
        print("7.5%")

class HDFC(Bank):
     def rateofIntrest(self):
            print("7%")

class Yes(HDFC):
     pass

s=SBI()
s.rateofIntrest()

i=IDBI()
i.rateofIntrest()

h=HDFC()
h.rateofIntrest()

y=Yes()
y.rateofIntrest()