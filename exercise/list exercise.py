l1 = ["amin", "amir", "ahmad", "babak", "ali", "mansoor"]
l2 = ["sara", "ehsan", "ahmad", "hasan", "ali", "hossain"]

# print([name for name in l if name[0]=="a"])
print(list(filter(lambda x: x if x[0] == "a" else None, l1)))
print(list(filter(lambda x: x[0] == "a", l1)))
print(list(filter(lambda x: len(x) == 4, l1)))
print(list(zip(l1, l2)))
