def my_for(iterable, func):
    iterable1 = iterable
    iterator = iter(iterable1)
    while True:
        try:
            func(next(iterator))
        except StopIteration:
            break

listam = [1, 2, 3, 4, 5, 6]
my_for(listam, print)
