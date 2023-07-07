x=4
y=4
z=y

print(id(x))
print(id(y))
print(id(z))

l=[1,2,3]
l2=l
l3=list(l)

print("l == l2  : ",l == l2)
print("l is l2  : ",l is l2)
print("l == l3  : ",l == l3)
print("l is l3  : ",l is l3)

print(id(l))
print(id(l2))
print(id(l3))