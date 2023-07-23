

class Shape:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def calc_area(self):
        pass

    def calc_perimeter(self):
        pass

    def info_show(self):
        info = ""
        for k, v in self.__dict__.items():
            info += k + ": " + str(v)
        return info

    def __str__(self):
        return self.__class__.__name__


class Square(Shape):
    def __init__(self, **kwargs):
        self.length = None
        super().__init__(**kwargs)

    def calc_area(self):
        return self.length**2

    def calc_perimeter(self):
        return self.length*4


s = Square(length=10)
print(s.calc_area())
print(s.calc_perimeter())
print(s.info_show())


