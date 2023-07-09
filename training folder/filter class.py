l = [1, 3, 5, 6, 434, 6, 2, 7, 13, 17, 65, 9, 8]

print(list(filter(lambda x:x % 2, l)))
print(list(filter(lambda x:x if x % 2!=0 else None, l)))
print(list(filter(lambda x:x % 2 != 0, l)))
print(list(filter(lambda x:not x % 2, l)))
print(7 % 2 != 0)