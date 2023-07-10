l = [9,8,7,6,5]
l = iter(l)
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))

x = range(10)
x = iter(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# print(list(x))

def my_gen():
    n = 9
    while n<17:
        yield n
        n += 1
k=my_gen()
print(next(k))      
print(next(k))       
print(next(k))       
 
print(list(my_gen()))