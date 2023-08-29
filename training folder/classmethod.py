class Person:
    
    x = 3
    def __init__(self) -> None:
        pass
    
    
    @classmethod
    def shower(cls):
        return cls.x
    
    def shower2(self):
        return self.x
    
    
ali = Person()

print(ali.x)
print(Person.x)
print(Person.shower2(ali))
print(Person.shower())