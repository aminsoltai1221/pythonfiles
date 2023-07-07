l=["hello","hell","heat","hello world"]
l2=list(zip(*l))
common_prefix=""
for i in l2:
    if len(set(i))!=1:
        break
    common_prefix+=i[0]
print(common_prefix)