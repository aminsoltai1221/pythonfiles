result = {}
expenses = {"A":3, "C":0, "G":3, "T":0}
def is_subset(test: str, wanted: str) -> bool:
    test = set(test)
    wanted = set(wanted)
    if test.issubset(wanted):
        return True
    return False

def is_sorted(test: str, wanted: str) -> bool:
    l_string = [i for i in test]
    # print(l_string)
    for i in wanted:
        if i == l_string[0]:
            l_string.pop(0)
        if l_string == []:
            return True
    return False

def expenses_calculator(wanted, test):
    total_expenses = 0
    for i in expenses.keys():
        total_expenses += (wanted.count(i) - test.count(i)) * expenses[i]
    return total_expenses

def min_calculator(wanted, dna):
    for i in range(len(dna), 0, -1):
        marker = 0
        while marker < len(dna) - i + 1:
            test = dna[0 + marker: i + marker]
            marker += 1
            if is_subset(test= test, wanted= wanted):
                if is_sorted(test, wanted):
                    final = dna[0: marker] + wanted + dna[i + marker:]
                    expense = expenses_calculator(wanted, test)
                    result[final] = expense
    return result

print(min_calculator(dna="TATA", wanted="CACA"))
#t print(is_subset("abc", "defanbmc"))
