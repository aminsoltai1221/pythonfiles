# number = "00??1100??1101?"
cases = ["1??1"]
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
                try:
                    cases.remove(number)
                except:
                    pass


# cases = [i for i in cases if "?" not in i]
# cases.sort(key = lambda x: int(x))
print(new_case)
print(cases)
