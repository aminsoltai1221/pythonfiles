class Person:
    person_number = 0

    def __init__(self, name, family):
        self.name = name
        self.family = family
        Person.person_number += 1


ahmad = Person("ahmad", "soltani")
amin = Person("amin", "soltani")
amir = Person("amir", "soltani")
ehsan = Person("ehsan", "soltani")

print(Person.person_number)
amin.person_number = 5
Person.person_number = 6
print(ahmad.person_number)
print(amir.person_number)
print(ehsan.person_number)
print(amin.person_number)

