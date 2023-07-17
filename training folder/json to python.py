import json

json_str1 = "null"
json_str2 = "true"
json_str3 = "7.6"
json_str4 = "[56,8,9,4]"
json_str5 = '"True"'
json_str6 = '"reza"'

python_obj1 = json.loads(json_str1)
python_obj2 = json.loads(json_str2)
python_obj3 = json.loads(json_str3)
python_obj4 = json.loads(json_str4)
python_obj5 = json.loads(json_str5)
python_obj6 = json.loads(json_str6)

print(json_str1, "\t", type(json_str1))
print(python_obj1, "\t", type(python_obj1))
print("---__"*30)
print(json_str2, "\t", type(json_str2))
print(python_obj2, "\t", type(python_obj2))
print("---__"*30)
print(json_str3, "\t", type(json_str3))
print(python_obj3, "\t", type(python_obj3))
print("---__"*30)
print(json_str4, "\t", type(json_str4))
print(python_obj4, "\t", type(python_obj4))
print("---__"*30)
print(json_str5, "\t", type(json_str5))
print(python_obj5, "\t", type(python_obj5))
print("---__"*30)
print(json_str6, "\t", type(json_str6))
print(python_obj6, "\t", type(python_obj6))
