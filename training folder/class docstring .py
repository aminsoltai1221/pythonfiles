class Pow:
    """
    its task is that and this class provides methods for getting something.
    >>>number1 = Pow(1, 3)
    1
    :param base: number that is bottom
    :param exponent: number that is up
    method:
        result:return number
    attribute none
    """
    def __init__(self, base: float, exponent: float) -> float:
        """
        :param base: number that is bottom
        :param exponent: number that is up
        """
        self.base = base
        self.exponent = exponent

    @property
    def result(self):
        return self.base ** self.exponent


print(Pow.__dict__)
# print(Pow.__dir__)
print(help(Pow))