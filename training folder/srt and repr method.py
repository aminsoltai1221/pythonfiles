class MyClass1:
    def __init__(self) -> None:
        self.a = 1
        self._b = 2
        self.__c = 3
    def __str__(self) -> str:
        return self.__class__.__name__
    
    def __repr__(self) -> str:
        return repr(self.__str__())
        

        
    
o1 = MyClass1()
o1.__c = 5
print(o1)
print(repr(o1))
