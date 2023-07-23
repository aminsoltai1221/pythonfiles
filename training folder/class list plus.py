class Mylist(list):
    def search(self, item):
        result = []
        for i in self:
            if type(item) == int:
                if item == i:
                    result.append(i)
            elif item in i:
                result.append(i)
        return result

    def append(self, item):
        # super.append()
        super().append(item)
        super().append(item)
        return self


l1 = Mylist([1, 2, 3, 4])
print(l1)
print(l1.search(4))
l1.append(5)
print(l1)
