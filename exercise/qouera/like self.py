from math import *
rows, columns = input("inpur rows and columns : ").split(" ")
scheme = []
for numbers in range(int(columns)):
    row = input("please input qutris table scheme : ").split()
    scheme.append(*row)
q = input("please input number of questions: ")
def calculator(accuration, column, row):
    for i in range(accuration-1):
        row = ceil(row / rows)
    index_row = row
    
print(scheme)
