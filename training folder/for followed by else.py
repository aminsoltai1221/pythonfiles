for i in range(4,34):
    n= 45
    if i % n == 0:
        print("there is one multiple")
        break
else:
    print(f"no number that is multiple of {n} found")