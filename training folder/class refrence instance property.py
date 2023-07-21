class Person:
    registered_users = []
    users_list = []
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        Person.registered_users.extend([self.name + " " + self.family])
        Person.users_list.append(self)
        # print(f"{self.name} {self.family} logged in")
     
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name},{self.family},{self.age})"   
    def __str__(self) -> str:
        return f"{self.name} {self.family} and age is {self.age}"
    @classmethod
    def users_show(self):
        print(Person.registered_users)

# Person.users_show()
ahmad = Person("ahmad", "soltani", 36)
amin = Person("amin", "soltani", 23)
amir = Person("amir", "soltani", 40)
ehsan = Person("ehsan", "soltani", 30)

# ehsan.users_show()
# Person.registered_users.append("zahra soltani")
# ehsan.users_show()
# amin.registered_users = ["ali soltani"]
# print(amin.registered_users)
# print(amir.registered_users)
# print(Person.registered_users)
# amin.users_show()
Person.users_show()
print(Person.users_list)
for i in Person.users_list:
    print(i)