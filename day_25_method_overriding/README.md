# Problem: Override the __str__ method for Book and EBook to display nicely.
## Solution:
- In main.py
## Notes:
- <h3><b>Core Concepts</b></h3>
    <strong> <code>__str__</code> Method </strong>: Built-in Python dunder (double underscore) method used for creating a clean, human-readable string representation of an object.<br>
    <strong>Implicit Calling</strong>: Triggered automatically when using <code>print(object)</code> or <code>str(object)</code>.<br>
    <strong><code>super()</code> Function</strong>: Accesses and calls methods from a parent class inside a child class.<br>
    <strong>DRY Principle</strong>: "Don't Repeat Yourself." Using <code>super().__str__()</code> allows the child class to reuse parent formatting without duplicating code.
- <h3><b>Code Execution Breakdown</b></h3>
    <strong>1. Base Class: <code>Book</code></strong> <br>
      Defines core attributes shared by all books: <code>title</code>, <code>author</code>, and <code>isbn</code>.<br>
      <code>__str__</code> formats basic details: <code>'Title' by Author - ISBN: Y.</code><br>
      <br>
    <strong>2. Subclass: <code>EBook(Book)</code></strong><br>
      Inherits all fields and methods from <code>Book</code>.<br>
      Adds digital-specific fields: <code>size</code>.<br>
      Uses <code>super().__init__()</code> to let the parent class handle basic initialization.<br>
      Uses <code>super().__str__()</code> to grab the parent text string, then appends file details using string interpolation (f-strings).<br>
