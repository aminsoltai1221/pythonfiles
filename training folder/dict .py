# n=int(input("numbers of colors :"))
# dict = {"color number" : "" , "amount" : 0 }
# for i in range(n):
#     c=input("input the number of your color:")
#     dict = dict + {"color number" :c ,"amount" : 1 }
# for item in dict.items():
#     print(item)

my_dict={"name":"ali" ,"family":"alavi","age":"61"}
my_dict2={"name2":"alireza" ,"family2":"alaa","age2":"56","c":6}

# print(my_dict)
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.popitem())
# print(my_dict)
# del my_dict
# print(my_dict)

dict3=dict.fromkeys([i for i in range(4)],[5,6,7,8,3])
print(dict3)
print(my_dict|my_dict2)

my_dict2["childrens"]=my_dict2.pop("c")
print(my_dict2)
my_dict.clear()


l = ["ali", "hasan", "hossain"]

dic4 = {name:[i for i in range(5)] for name in l}

print(dic4)