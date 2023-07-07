def my_func():
    b = 10
    def func2():
        a = 5
    print(a)

my_func()

c=54
def my_func2():
    c=60
    print(c)

print(c)
my_func2()


def func3():
    global x
    x=64


# func3()
print(x)