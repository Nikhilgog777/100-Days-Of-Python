#  Create a greet_user(name) function with a default argument "Guest".

def greet_user(name = "Guest"):  # function definition with Guest as default argument
    print(f"Hello {name}")

name = input("Enter your name : ")

greet_user(name)  # Function call