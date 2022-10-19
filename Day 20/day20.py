# Python has three types of access modifiers:

# Public Access Modifier         self.a
# Protected Access Modifier      self._a
# Private Access Modifier        self.__a

class Test:
        __pass=""

        def setPass(self,p):
            self.__pass=p

        def getPass(self):
            return self.__pass


t=Test()

t.__pass="abbc123"

# t.setPass("abc123")

print(t.__pass)



