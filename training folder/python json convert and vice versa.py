import json

name = "ali"
lastname = "alavi"
age = 57
courses = ["physics", "math"]
bachelor = False

d = dict(name=name, lastname=lastname, age=age, courses=courses, bachelor=bachelor)
with open("json_test.json", "w") as jf:
    json.dump(d, jf)

with open("json_test.json", "r") as f:
    s = json.load(f)

print(s)
