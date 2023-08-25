global_var = 15
def my_function():
    print(global_var)
my_function()  # Output: 15
print(global_var)  # Output: 15
global_var = 15



def my_function():
    print(global_var)
my_function()  # Output: 15
print(global_var)  # Output: 15
print(len([1, 2, 3]))  # Output: 3
# 'len' is a built-in function accessible from anywhere
print(len([1, 2, 3]))  # Output: 3
# 'len' is a built-in function accessible from anywhere



global_var = 10
def outer_function():
    outer_var = 5
    def inner_function():
        inner_var = 3
        print("inner_var:", inner_var)  # Output: inner_var: 3
        print("outer_var:", outer_var)  # Output: outer_var: 5
        print("global_var:", global_var)  # Output: global_var: 10
    inner_function()
    print("outer_var:", outer_var)  # Output: outer_var: 5
outer_function()
print("global_var:", global_var)  # Output: global_var: 10





# Accessing inner_var, outer_var here would result in errors
global_var = 10
def outer_function():
    outer_var = 5
    def inner_function():
        inner_var = 3
        print("inner_var:", inner_var)  # Output: inner_var: 3
        print("outer_var:", outer_var)  # Output: outer_var: 5
        print("global_var:", global_var)  # Output: global_var: 10
    inner_function()
    print("outer_var:", outer_var)  # Output: outer_var: 5
outer_function()
print("global_var:", global_var)  # Output: global_var: 10
# Accessing inner_var, outer_var here would result in errors
def my_function():
    local_var = 10
    print(local_var)
my_function()  # Output: 10
# Accessing local_var here would result in an error
def my_function():
    local_var = 10
    print(local_var)
my_function()  # Output: 10
# Accessing local_var here would result in an error



def outer_function():
    outer_var = 5
    def inner_function():
        nonlocal outer_var  # Declare outer_var as nonlocal
        inner_var = 3
        print("inner_var:", inner_var)  # Output: inner_var: 3
        print("outer_var (before modification):", outer_var)  # Output: outer_var (before modification): 5 
        outer_var = 7  # Modify outer_var using nonlocal
        print("outer_var (after modification):", outer_var)  # Output: outer_var (after modification): 7
    inner_function()
    print("outer_var (outside inner_function):", outer_var)  # Output: outer_var (outside inner_function): 7
outer_function()







global_var = 10  # Global variable
def outer_function():
    outer_var = 5  # Enclosing (local) variable
    
    def inner_function():
        nonlocal outer_var  # Declare outer_var as nonlocal
        inner_var = 3  # Local variable
        global global_var  # Declare global_var as global
        print("inner_var:", inner_var)  # Output: inner_var: 3
        print("outer_var (before modification):", outer_var)  # Output: outer_var (before modification): 5
        print("global_var:", global_var)  # Output: global_var: 10
        outer_var = 7  # Modify outer_var using nonlocal
        global_var = 15  # Modify global_var
        print("outer_var (after modification):", outer_var)  # Output: outer_var (after modification): 7
        print("global_var (after modification):", global_var)  # Output: global_var (after modification): 15
    inner_function()
    print("outer_var (outside inner_function):", outer_var)  # Output: outer_var (outside inner_function): 7
outer_function()
print("global_var (outside outer_function):", global_var)  # Output: global_var (outside outer_function): 15




