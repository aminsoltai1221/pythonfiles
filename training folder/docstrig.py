def max3(x:int, y:int, z:int) -> int:
    """receives three number as input and return max of them
    
    Parameters:
        x (int): An decimal integer
        y (int): An decimal integer
        z (int): An decimal integer
    
    Returns:
        max_int (int): largest of them
    """
    return max(x, y, z)

print(max3.__doc__)
# print(help(max3))
print(max3.__annotations__)