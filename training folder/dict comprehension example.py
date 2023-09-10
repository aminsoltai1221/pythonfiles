my_dict={"name":"ali" ,"family":"alavi","age":61}
d2 = {k:v for k,v in my_dict.items() if type(v) == int}
print(d2)