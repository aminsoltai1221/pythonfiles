def myenumerate(l):
    n=1
    while n<=len(l):
        yield n,l[n-1]
        n+=1

l = ["a","b","c","d"]

for i,j in myenumerate(l):
    print(i,j)