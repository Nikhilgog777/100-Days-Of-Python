# Problem: Build a “password strength checker” that checks length, uppercase, digits, and special chars.
## Solution: 
- In main.py
## Notes: 
- ```import string``` is Python's module which provides predefined character constants.
- For a strong password, the length of password should be atlest 8. So, the condition of length greater than equal to 8 is used.
- ```has_upper```, ```has_lower```, ```has_digits``` and ```has_special``` checks for the respective conditions.
- Since all the conditions should be true so we have to return all the conditions
- In the print statement ascii characters are used to print the ```WELCOME``` message
