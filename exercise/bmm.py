x = int(input("number 1 :"))
y = int(input("number 2 :"))

b = max(x, y)
k = min(x, y)
# bmm = 1
if b % k == 0:
    print(k)
else:
    for i in range(1,int((k/2) + 1)):
        if k % i == 0 and b % i == 0:
            bmm = i   
    print(bmm) 