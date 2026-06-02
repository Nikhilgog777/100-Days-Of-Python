#  Write a factorial(n) function using recursion. Add a try/except for negative inputs.

def factorial(n):
    try:
        if n < 0 :
            raise ValueError("Factorial is not defined for negative numbers.")
    except ValueError as e:
        print(f"Input Error : {e}")
        return None
    if n == 0 or n == 1 :
        return 1
    else :
        return n * factorial(n-1)
    
num = factorial(-5)
print(num)