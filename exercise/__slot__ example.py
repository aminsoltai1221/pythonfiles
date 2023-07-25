import timeit


class MyClass:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class SlotClass:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# Test performance of MyClass
my_object = MyClass(1, 2, 3)
elapsed_time = timeit.timeit(lambda: MyClass(1, 2, 3), number=1000000)
print(f"MyClass: {elapsed_time:.6f} seconds")

# Test performance of SlotClass
slot_object = SlotClass(1, 2, 3)
elapsed_time = timeit.timeit(lambda: SlotClass(1, 2, 3), number=1000000)
print(f"SlotClass: {elapsed_time:.6f} seconds")
