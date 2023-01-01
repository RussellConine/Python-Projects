class Protected:
    def __init__(self):
        self._protectedVar = 0


obj = Protected()
obj._protectedVar = 34
# print(obj._protectedVar)


class Further_Protected:
    def __init__(self):
        self.__privateVar = 12
    
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private

obj2 = Further_Protected()
obj2.getPrivate()
obj2.__privateVar = 23
obj2.getPrivate()
print(obj2.__privateVar)
obj2.getPrivate()

# obj2.__privateVar = 10
# print(obj2.__privateVar)