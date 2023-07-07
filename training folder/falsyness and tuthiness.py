l=[1,2,3,4,5]
l2=l.copy()
l3=l
l4=list(l)
s="hi"
# s2=s.copy()
s3=s
dic={1:"ali"}
dic2=dic.copy()
dic3=dic


print(l is l2)
print(l is l3)
print(l is l4)

print(s is s3)

print(dic is dic2)
print(dic is dic3)