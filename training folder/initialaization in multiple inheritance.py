class Employees:
    def __init__(self, name, family, phone, person_number, **kwargs) -> None:
        self.name = name
        self.family = family
        self.phone = phone
        self.person_number = person_number


class Manager(Employees):
    def __init__(self, wage, **kwargs) -> None:
        super().__init__(**kwargs)
        self.wage = wage


class Teachers(Employees):
    def __init__(self, courses: list, **kwargs) -> None:
        super().__init__(**kwargs)
        self.courses = courses


class TeacherManager(Teachers, Manager):
    def __init__(self, teaching_time: float, **kwargs) -> None:
        super().__init__(**kwargs)
        self.teaching_time = teaching_time


man1 = TeacherManager(name="amin", family="soltani", phone=9901491003, person_number=94060667, wage=10,
                      courses=["physics"], teaching_time=6)
print(man1.family)
