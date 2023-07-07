a="42"
print(a.zfill(10))

name,dic="amin soltani",{}
for i in name.replace(" ",""):
    dic[i]=name.count(i)
for key,value in dic.items():
    print(f"your name has {value} {key}")