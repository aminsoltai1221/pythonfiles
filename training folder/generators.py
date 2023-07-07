def mogenerator():
    yield 1
    yield 2
    yield 3


x = mogenerator

print(mogenerator)
print(mogenerator())
print(list(x()))
print(list((i for i in range(5))))
print((i for i in range(5)))