cases = ["1?0??0?1"]
num = cases[0]
new_case = cases
while True:
    for i in new_case:
        if "?" in i:
            break
    else:
        break
    cases = new_case
    new_case = []
    for number in cases:
        for i in number:
            if i == "?":
                number1 = number[:number.index(i)] + "1" + number[number.index(i) + 1:]
                number2 = number[:number.index(i)] + "0" + number[number.index(i) + 1:]
                new_case.append(number1)
                new_case.append(number2)                
                break
            
print(new_case)
print(len(set(new_case)))
