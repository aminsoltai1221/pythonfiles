x = int(input("number 1 :"))
y = int(input("number 2 :"))

b = max(x, y)
k = min(x, y)

for i in range(1,k + 1):
    if (b * i)%k==0:
        break
print(b*i)