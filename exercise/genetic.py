

def is_subset(string: str, refr: str) -> bool:
    if set(string).issubset(set(refr)):
        return True
    return False
def is_sorted(string: str, refr: str) -> bool:
    num = 0
    l_string = [i for i in string]
    print(l_string)
    for i in refr:
        if i == l_string[num]:
            l_string.pop(num)
    if l_string:
        return False
    return True

# print(is_subset("abc", "defanbmc"))

