# def say_hello(func):
#     def wrapper(name):
#         print("this is before func execution")
#         func(name)
#         print("this is after func execution")
#     return wrapper
# # def hello(name):
# #     print(f"hello {name}")
# # hello = say_hello(hello)
# # hello()
# @say_hello
# def hello(name):
#     print(f"hello {name}")
# hello("amin")

# def outer(func,number):
#     return func(number)
#
#
# def inner(number):
#     print(number)
#
#
# inner2=outer(inner,6)
# inner2


# def outer2(func):
#     def wrapper():
#         print("before func execution in outer2")
#         print(func())
#         print("before func execution in outer2")
#     return wrapper
# # def outer1(func):
# #     def wrapper():
# #         print("before func execution in outer1")
# #         x=func()
# #         print(x)
# #         print("before func execution in outer1")
# #     return wrapper
# @outer2
# # @outer1
# def test():
#     return 5

# test()









def outer_drcorator(name):
    def inner_decorator(func):
        def wrapper():
            print("hhhh")
            return func(name)
        return wrapper
    return inner_decorator


@outer_drcorator("ali")
def say_hello(name):
    return f"hi {name}"

print(say_hello())








def outer(permission):
    if permission:
        def decorator(func):
            wraps(func)
            def inner(name):
                print()
                print("*" * 10)
                print(func(name))
                print("*" * 10)
                print()
            return inner
        return decorator
        
 
@outer(1)  
def helloname(name):
    return f"hi {name} !"




helloname("amir")