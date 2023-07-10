def adder(l):
    n=0
    for i in l:
        n+=i
        yield n


l=[1,2,3,4,5]
for i in adder(l):
    print(i)
    
def numbersaz():
    n=1
    while True:
        n+=i
        yield int(str(n)*n)

for i in range(6):
    print(next(numbersaz()))