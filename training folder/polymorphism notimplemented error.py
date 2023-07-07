class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def info_show(self):
        raise NotImplementedError


class User(Person):
    def __int__(self, name, family):
        super.__init__(name, family)

    def info_show(self):
        print(self.name + " " + self.family)


class Manager(Person):
    def __int__(self, name, family):
        super.__init__(name, family)

    # def info_show(self):
    #     print(self.name + " " + self.family)


manager1 = Manager("amir", "soltani")
user1 = User("amin", "soltani")


user1.info_show()
manager1.info_show()