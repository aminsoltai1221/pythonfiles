def doubler(a):
    def nested(b):
        return a*b
    return nested

number=doubler(4)
print(number(3))