dic = {'ali': 1, 'hasan': 2, 'hossain': 3, "sajjad": 4, "mohammad": 5, "jafar": 6}
print(dic)
l = [i for i in dic.items()]
l.sort(key=lambda x:x[1])
print(l)
print(dict(l))