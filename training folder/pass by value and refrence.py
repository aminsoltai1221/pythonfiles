a = "ali"
def heydar(a):
    a += " heydar"
    print(a)
    
#for immutable like top

    
#but for mutable is pass by refrence and object will change like this    
l = [1, 2, 3]    
def addition(a):
    a += [4,5,6]
    print(a)
    
heydar(a)
print(a)

print("-"*10)

addition(l)
print(l)