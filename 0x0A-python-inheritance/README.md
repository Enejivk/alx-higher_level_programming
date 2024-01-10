# 0x0A. Python - Inheritance

## Description

This project focuses on the concept of inheritance in Python and its implementation. It covers topics such as superclass, subclass, method overriding, multiple inheritance, and the use of built-in functions like isinstance, issubclass, type, and super.

## Learning Objectives

At the end of this project, you are expected to be able to explain without external help:
- Why Python programming is awesome
- What is a superclass, base class, or parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- When and how to use isinstance, issubclass, type, and super built-in functions

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- Length of files will be tested using wc
- Python Test Cases
  - All test files inside a folder named tests
  - All test files are text files (extension: .txt)
  - All tests executed using the command: `python3 -m doctest ./tests/*`
  - Modules, classes, and functions should have documentation

### Documentation
- Avoid using the words import or from inside comments

## Quiz Questions

Great! You've completed the quiz successfully! Keep going! (Show quiz)

## Tasks

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object:

Prototype: `def lookup(obj):`
Returns a list object
You are not allowed to import any module

### 1. My list
Write a class MyList that inherits from list:

Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module

### 2. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.

Prototype: `def is_same_class(obj, a_class):`
You are not allowed to import any module

### 3. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

Prototype: `def is_kind_of_class(obj, a_class):`
You are not allowed to import any module

### 4. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

Prototype: `def inherits_from(obj, a_class):`
You are not allowed to import any module

### 5. Geometry module
Write an empty class BaseGeometry.

You are not allowed to import any module

### 6. Improve Geometry
Write a class BaseGeometry (based on 5-base_geometry.py).

Public instance method: `def area(self):` that raises an Exception with the message area() is not implemented
You are not allowed to import any module

### 7. Integer validator
Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: `def area(self):` that raises an Exception with the message area() is not implemented
Public instance method: `def integer_validator(self, name, value):` that validates value:
  - You can assume name is always a string
  - If value is not an integer: raise a TypeError exception, with the message `<name> must be an integer`
  - If value is less or equal to 0: raise a ValueError exception with the message `<name> must be greater than 0`
You are not allowed to import any module

### 8. Rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: `def __init__(self, width, height):`
  - Width and height must be private. No getter or setter
  - Width and height must be positive integers, validated by integer_validator

### 9. Full rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: `def __init__(self, width, height):`
  - Width and height must be private. No getter or setter
  - Width and height must be positive integers validated by integer_validator
  - The area() method must be implemented
  - `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

### 10. Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py):

Instantiation with size: `def __init__(self, size):`
  - Size must be private. No getter or setter
  - Size must be a positive integer, validated by integer_validator
  - The area() method must be implemented

### 11. Square #2
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: `def __init__(self, size):`
  - Size must be private. No getter or setter
  - Size must be a positive integer, validated by integer_validator
  - The area() method must be implemented
  - `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

## Author
By: Guillaume