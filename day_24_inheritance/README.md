# Problem: Use inheritance: make EBook (subclass of Book) with an extra file_size attribute.
## Solution:
- In main.py
## Notes:
- <strong> Code Purpose </strong>: It models books by creating a base class and expanding it for digital versions.
- <strong> Inheritance Definition </strong>: A mechanism where a child class copies attributes and methods from a parent class.
- <strong> Parent Class (`Book`) </strong>: The base template containing shared data like `title` and `author`.
- <strong> Child Class (`EBook`) </strong>: The specialized template that inherits from `Book` and adds `file_size`.
- <strong> The `super()` Function </strong>: A built-in command that runs the parent class initialization code to prevent rewriting code.
- <strong> Method Overriding </strong>: Redefining `get_info()` in `EBook` to replace the parent version and print the extra file size details.
- <strong> Code Reusability </strong>: Inheritance saves time because you only write core book logic once.
