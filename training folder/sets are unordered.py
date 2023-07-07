set1={"car","suit","carrot"}
set2={"card","suite","carrot"}
print(set1-set2)
print(set1|set2)
print(set1&set2)
print(set1.union(set2))

set1.update(set2)
print(set1)

set1.remove("card")
set1.discard("hat")

l=[1,2,3,4,5,6,7,8,9]
setNumbers={0}
setNumbers.update(l)
print(setNumbers)