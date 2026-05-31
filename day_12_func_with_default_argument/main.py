#  Create a greet_user(name) function with a default argument "Guest".

def greet_user(name = "Guest"):  # function definition with Guest as default argument
    print(f"Hello {name}")

greet_user() # Prints the default "Guest"

name = input("Enter your name : ")
greet_user(name)  # Prints the variable name
