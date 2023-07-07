def test(func):
    return func


def test2(number):
    print(number + 8)


func = test(test2)
func(4)