from random import randrange   



print(x:=54)  #  assign 54 to x and then print it

l=[]
while (s := input("pleae take your move!") != "exit"):
    l.append(s)
    
    
 
 
f = lambda :randrange(50,150)    
print([l for i in range(10) if (l:=f())>100])