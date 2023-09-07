# print(1 or "" or [] or 2)
# print(5 and 6 and [] and 3)




# a = [1, 2, 3, 4]
# b = [12, 43, 56, 78]
# for i,j in zip(a,b):
#     print(i, j) 


x = 4
y = 5
z = 1
def A():
    print(x)
    z = 9
    def B():
        print(y)
        print(z)
    
    B()


A()    
    