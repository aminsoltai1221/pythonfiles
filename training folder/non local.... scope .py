a = 5
def fun2():
    print("fun2")
def func():
    fun2()
    global a
    print(a)
    a = 8
    print(a)

print(a)

func()
print(a)