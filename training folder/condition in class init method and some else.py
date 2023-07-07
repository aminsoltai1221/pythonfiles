class Person:
    def __init__(self, name, family, age) -> None:
        self.name=name 
        self.family=family
        if age>18:
            self.age=age
        else:
            raise ValueError
        
        

you=Person("amin", "soltani", 20)
you.age=15
print(you.age)