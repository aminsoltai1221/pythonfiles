l=[1,2,3,4,5,6,7,8,9]
print(l[:4:-1])

print(l[3::-1])

print([i if i%2==0 else ("-" if i%3==0 else " No") for i in range(11)])