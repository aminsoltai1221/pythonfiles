dict1 = {"ali": 1, "hasan": 2, "hossain": 3}
d = {1: 'ali', 2: 'hasan', 3: 'hossain'}

print({dict1[k]:k for k in dict1.keys()})

l = {**dict1,**d}
print(l)