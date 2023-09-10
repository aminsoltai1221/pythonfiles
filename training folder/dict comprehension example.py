my_dict={"name":"ali" ,"family":"alavi","age":61}
d2 = {k:v for k,v in my_dict.items() if type(v) == int}
print(d2)




l1 = [1, 2, 3, 4]
l2 = ["ali", "hasan", "hossain"]
d2 = {k:v for k,v in zip(l1, l2) if not type(v) == int}
print(d2)