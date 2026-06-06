# Use a lambda function with map() to square a list of numbers.

# Original List of numbers
numbers = [1, 4, 3, 5, 12, 9]

# Lambda function for square
square = list(map(lambda x : x*x, numbers))

# Print square
print(square)

