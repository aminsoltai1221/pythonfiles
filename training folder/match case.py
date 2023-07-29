from random import randint

x = randint(10)
y = randint(10)

match (x, y):
    case (5, 5):
        print("good")
    case (6, 6):
        print("excellent")
    case (1, 1):
        print("bad")
    case (2, y) | (7, y):
        print("mediocre")
    case (4, 4):
        print("better")
    case (x, 5) | (7, x) if x == y:
        print("")
    case (int(), int()):
        print("are integers")
