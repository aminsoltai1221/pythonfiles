def log2(number):
    result = 0
    while number > 1:
        number /= 2
        result += 1
        if number < 2:
            break
    print(number)
    print(result)

log2(75)
log2(64)
log2(255)
log2(1)