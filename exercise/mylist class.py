class New_list(list):

    @property
    def average(self):
        try:
            avg = sum(self) / len(self)
            return avg
        except TypeError:
            return "Average is not reachable"


l1 = New_list([1, 5, 7, "k", 7])
print(l1.average)
