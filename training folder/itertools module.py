from itertools import permutations,combinations,product


my_list = [1,2,3,4]

print(list(product(my_list, repeat=2)))
#[(1, 1),(1, 2),(1, 3),(1, 4),(2, 1),(2, 2),
# (2, 3),(2, 4),(3, 1),(3, 2),(3, 3),(3, 4),(4, 1),(4, 2),(4, 3),(4, 4)]
print("*" * 20)

print(list(permutations(my_list, 3)))
print("*" * 20)
print(list(combinations(my_list, 2)))
