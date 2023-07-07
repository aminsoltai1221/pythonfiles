dict1={"number":1 ,"age":23 ,"weight":46} 
dict2=dict1
dict2["height"]=2
print(dict1 is dict2)
print(dict1)
print("___________--------------___________________--------------------")
l1=[1,2,3,4,5]
l2=l1
l2.append(6)
print(l1)
print(l1 is l2)
print("___________--------------___________________--------------------")
string1="abc"
string2=string1
print(string1 is string2)
string2+="d"
print(string2)
print(string1)
print("___________--------------___________________--------------------")
set1={1,2,3,4,5}
set2=set1
print(set1 is set2)
set2=set2.union([5,6])
print(set2)
print(set1)
print("___________--------------___________________--------------------")
tup1=(1,2,3,4,5)
tup2=tup1
print(tup1 is tup2)

'''
just for lists and dictionaries changes in copy effects in origin instance
'''