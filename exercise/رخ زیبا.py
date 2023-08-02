def is_happy():
    coordinates = []
    for i in range(4):
        x, y = input("please input x and y (seperated by space) :  ").split()
        if [x, y] in coordinates:
            x, y = input("please input x and y (seperated by space) :  ").split()
        coordinates.append([x, y])
    if len(set((set(coordinates[0] + coordinates[1]) & set(coordinates[2] + coordinates[3])))) == 1:
        return "happy"
    return "unhappy"
print(is_happy())

