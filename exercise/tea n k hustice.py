import random
def column_state(n, k):
    minimum = k // n
    numberofplus1 = k % n
    remain = n - numberofplus1
    column = [minimum for number in range(remain)] + [(minimum+1) for number in range(numberofplus1)]
    dic_columns = {1:column}
    for i in range(n):
        x = column.pop(-1)
        column = [x] + column
        print(column)
column_state(8,55)