def fact(n):
    if n == 1:
        return 1
    result = n * fact(n-1)
    return result 

print(fact(5))

def fibonacci(n):
    if n ==1 or n==2:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    return result

for i in range(1,10):
    print(fibonacci(i))
    