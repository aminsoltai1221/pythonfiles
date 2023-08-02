rows, columns = input("please input rows and columns separated by space : ").split()
cor = []
rows = int(rows)
columns = int(columns)
for i in range(rows):
    args = input("please input points status : ").split()
    cor.append(args)


def is_winner():
    row = cor
    row_result = [[h[t] for h in cor] for t in range(columns)]
    diameter = [cor[o][o] for o in range(columns)]
    diameter2 = [cor[o][columns - o - 1] for o in range(columns)]
    raws_columns_diameter = []
    for item in (diameter, row_result, row, diameter2):
        if item == diameter or item == diameter2:
            string = "".join(item)
            raws_columns_diameter.append(string)
            if "xxx" in string or "ooo" in string:
                return "finished"
        else:
            for lists in item:
                string = "".join(lists)
                raws_columns_diameter.append(string)
                if "xxx" in string or "ooo" in string:
                    return "finished"
    print(raws_columns_diameter)
    o_cases = {"oo_", "o_o", "_oo"}
    x_cases = {"xx_", "x_x", "_xx"}


print(is_winner())
