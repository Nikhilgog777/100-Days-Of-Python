#  Print the first 10 Fibonacci numbers using a while loop.
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Initialize the first two Fibonacci numbers
a, b = 0, 1
count = 0

# Print the first 10 numbers using a while loop
while count < 10:
    print(a, end=" ")
    
    # Calculate the next number and update variables
    next_num = a + b
    a = b
    b = next_num
    
    count += 1