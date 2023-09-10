import copy

# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Shallow copy
shallow_copy = original_list.copy()

# Deep copy
deep_copy = copy.deepcopy(original_list)

# Modify the original list
original_list[0][0] = 'X'

print("Original list:", original_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)


# Original list: [['X', 2, 3], [4, 5, 6], [7, 8, 9]]
# Shallow copy: [['X', 2, 3], [4, 5, 6], [7, 8, 9]]
# Deep copy: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]