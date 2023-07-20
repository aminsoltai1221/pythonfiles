x = "Is true" if True else "Is false"
print(x)

print(True if 2 > 1 else False)
print(2 > 1 and True or False)
print(False if 2 > 1 else True)
print(2 > 1 and False or True)
x = -1
print('x is less than zero' if x < 0 else 'x is greater than zero' if x > 0 else 'x is equal to 0')

t = 90
print('Water is boiling' if t >= 100 else 'Water is not boiling')

t = 90
print(('Water is not boiling', 'Water is boiling')[t >= 100])
print({True: 'Water is boiling', False: 'Water is not boiling'}[t >= 100])
print((lambda: 'Water is not boiling', lambda: 'Water is boiling')[t >= 100]())
