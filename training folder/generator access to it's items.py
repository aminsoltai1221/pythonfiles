# def gen():
#     yield 1
#     yield 2
    
# print(list(gen()))
# print(set(gen()))
# print(tuple(gen()))
# print(sum(gen()))
# for i in gen():
#     print(i)
    
    
# x = iter(gen())
# print(next(x))
# print(next(x))


def fib(s):
    a = 0
    b = 1
    while a < s:
        yield a
        x = a
        a = a + b
        b = x
    
for i in fib(789):
    print(i)