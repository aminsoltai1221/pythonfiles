# 0 1 1 2 3 5 8 13 21 ...

# def fibonacci(max):
#     a=0
#     b=1
#     while a < max:
#         print(a)
#         a,b=a+b,a
        
def fibonacci(max):
    a=0
    b=1
    while b < max:
        print(a)
        print(b)
        a = a+b
        b=a + b
fibonacci(19)

