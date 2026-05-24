# Problem : Write a program that takes two numbers as input and prints their sum, difference, product, and quotient.

## Sotution :
a = int(input("Enter first number : ")) <br>
b = int(input("Enter second number : ")) <br>

#Arithmetic function <br>
sum = a+b <br>
difference = a-b <br>
product = a*b <br>
quotient = a/b <br>

print(f'''The sum is {sum}. <br>
The difference is {difference}. <br>
The quotient is {quotient}. <br>
The product is {product}.''' <br>
) 

## Notes : 
- Used input() function to get the input from the user
- By using typecasting changed the input into integer
- Created variables for all the arithmetic calculations
- Printed all the arithmetics using f-strings in print()
- Used triple quotes for multi-lines strings 
