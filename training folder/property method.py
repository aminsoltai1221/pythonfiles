class Person:
    def __init__(self, name, family, age):
        self.name=name 
        self.family=family
        if age > 18:
            self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 18:
            self._age = value
            
    @age.getter
    def age(self):
        return self._age       
        
you=Person("amin", "soltani", 20)
print(you.age)
you.age=23
print(you.age)
