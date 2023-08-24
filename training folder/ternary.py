x = "Is true" if True else "Is false"
print(x)

print(True if 2 > 1 else False)
print(2 > 1 and True or False)
print(False if 2 > 1 else True)
print(2 > 1 and False or True)
x = -1
print('x is less than zero' if x < 0 else 'x is greater than zero' if x > 0 else 'x is equal to 0')

t = 90
print('Water is boiling' if t >= 100 else 'Water is not boiling')

t = 90
print(('Water is not boiling', 'Water is boiling')[t >= 100])
print({True: 'Water is boiling', False: 'Water is not boiling'}[t >= 100])
print((lambda: 'Water is not boiling', lambda: 'Water is boiling')[t >= 100]())

# Define a lambda function with ternary condition
f = lambda x: "Positive" if x > 0 else "Negative or Zero"

# Test the function
print(f(10))  # Output: Positive
print(f(-5))  # Output: Negative or Zero
print(f(0))   # Output: Negative or Zero

# Define a list of numbers
numbers = [1, -2, 3, -4, 5]

# Use a list comprehension with a lambda function to classify the numbers
classification = [(lambda x: "Positive" if x > 0 else "Negative")(x) for x in numbers]

print(classification)  # Output: ['Positive', 'Negative', 'Positive', 'Negative', 'Positive']




# Define a list of numbers
numbers = [1, -2, 3, -4, 5]

# Use a map function with a lambda function to classify the numbers
classification = list(map(lambda x: "Positive" if x > 0 else "Negative", numbers))

print(classification)  # Output: ['Positive', 'Negative', 'Positive', 'Negative', 'Positive']