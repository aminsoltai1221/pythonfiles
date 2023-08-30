# 0 1 1 2 3 5 8 13 21 ....
def fib(max):
    maximum = max
    a = 0
    b = 1
    while a < maximum:
        print(a)
        a, b = a+b, a
        

# fib(18)
