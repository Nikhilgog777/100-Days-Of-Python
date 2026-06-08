# Build a “password strength checker” that checks length, uppercase, digits, and special chars.

import string

def password_checker(password):
    if len(password) < 8:
        return False
    
    # Checks all conditions independently
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$^&*_" for c in password)
    
    # All three must be true
    return has_upper and has_lower and has_digit and has_special

print('''
╻   ┏━┓┏━┓┏━┓┏━┓╻ ╻┏━┓┏━┓╺┳┓   ┏━╸╻ ╻┏━╸┏━╸╻┏ ┏━╸┏━┓   ╻
┃   ┣━┛┣━┫┗━┓┗━┓┃╻┃┃ ┃┣┳┛ ┃┃   ┃  ┣━┫┣╸ ┃  ┣┻┓┣╸ ┣┳┛   ┃
╹   ╹  ╹ ╹┗━┛┗━┛┗┻┛┗━┛╹┗╸╺┻┛   ┗━╸╹ ╹┗━╸┗━╸╹ ╹┗━╸╹┗╸   ╹   
      ''')

while True:
    password = input("Enter your password : ")
    if(password_checker(password) == True):
        print("Your password is strong.")
        break
    else:
        print("Weak password. Try different password")