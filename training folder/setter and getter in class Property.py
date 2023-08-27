# class Person:
#     def __init__(self) -> None:
#         self.__age=None
#     def get_age(self):
#         return self.__age
#     def set_age(self,number):
#         self.__age = number
#     def del_age(self):
#         del self.__age
#     age = property(get_age, set_age, del_age)
    
    
    
class Person:
    def __init__(self) -> None:
        self.__age = 30 
    @property    
    def age(self):
        return self.__age
    @age.setter
    def age(self,number):
        self.__age = number
    @age.deleter
    def age(self):
        del self.__age




    
ali=Person()

# print(ali.get_age())
# ali.set_age(28)
# print(ali.get_age())

print(ali.age)
ali.age = 40
print(ali.age)