class Counter:

    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += self.step
            return result
        raise StopIteration


counter1 = Counter(5, 20, 3)
iter(counter1)
for num in counter1:
    print(num)

