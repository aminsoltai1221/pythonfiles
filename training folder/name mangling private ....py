class Person:
    def __init__(self, name, password, age):
        self.name = name  # public
        self._age = age  # protected
        self.__password = password  # private

    def __get_age__(self):
        print(f"age is equal to {self.age}")


me = Person("amin", "123456", 23)
print(me.name)
print(me._age)
print(me._Person__password)
