class Person:
    def __init__(self) -> None:
        self.b=1        #public
        self.__c = 4    #private
        self._d = 5     #protected   
        self.__a__ = 3   
        


amin = Person()

print(amin.b)

print(amin._d)

print(amin.__a__)

print(amin.__c)
