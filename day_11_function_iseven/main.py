#  Define a function is_even(n) that returns True if the number is even. Test it.
 
def is_even(n) : 
    if(n % 2 == 0):
        return True
    else:
        return False

num = int(input("Enter the number : "))

print(is_even(num))