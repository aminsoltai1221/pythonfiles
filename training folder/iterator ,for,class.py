class Myrange:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.b = 0
        return self

    def __next__(self):
        if self.b < self.number:
            x = self.b
            self.b += 1
            return x

        else:
            raise StopIteration


num = Myrange(7)
for i in num:
    print(i)