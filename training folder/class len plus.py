class Lenplus(len):
    def checker(self):
        if "__len__" in dir(self):
            return super(self)
        else:
            print("there is no this method")

