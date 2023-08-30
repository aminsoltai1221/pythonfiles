class Person:
    pass


class User:
    pass


class Student(User, Person):
    pass


s1 = Student()


print(Student.mro())
print(Student.__mro__)
# print(help(Student))
