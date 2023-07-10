
def my_decorator(func):
    memory = {}
    def wrapper(n):
        if n not in memory:
            memory[n]=func(n)
        return memory[n]
    return wrapper
        

@my_decorator
def fibonacci(n):
    if n ==1 or n==0:
        return n
    result = fibonacci(n-1) + fibonacci(n-2)
    return result

print(fibonacci(450))