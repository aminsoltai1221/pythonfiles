def func(*numbers):
    print(numbers)
    print(sum(numbers))
    
func(1,2,4,5,6,6)

def func2(list):
    print(list)
    print(sum(list))
    
func2([1,2,34,4,56,6])

l1=[1,2,3,4]
l2=[5,6,7]
l3=[8,9]

print([*l1,*l2,*l3])
print([l1,l2,l3])