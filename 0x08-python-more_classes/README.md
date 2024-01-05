# THIS ARE ALL THE QUESTIONS

## 0x08. Python - More Classes and Objects

### Project Overview
- **Title:** Python - More Classes and Objects
- **Language:** Python
- **Topic:** Object-Oriented Programming (OOP)
- **Author:** Guillaume
- **Weight:** 1

### Project Timeline
- **Project Start:** Jan 4, 2024, 6:00 AM
- **Project End:** Jan 5, 2024, 6:00 AM
- **Checker Release:** Jan 4, 2024, 12:00 PM
- **Auto Review Deadline:** Jan 5, 2024, 6:00 AM

### Resources
Read or watch:
- Object Oriented Programming (Read everything until the paragraph “Inheritance” (excluded))
- Object-Oriented Programming (Selected paragraphs for better understanding)
- Class and Instance Attributes
- Classmethods and Staticmethods
- Properties vs. Getters and Setters (Mainly the last part “Public instead of Private Attributes”)
- str vs repr

### Learning Objectives
At the end of this project, you are expected to be able to explain:
- Why Python programming is awesome
- What is OOP
- Concepts such as "first-class everything," class, object, instance, attribute, self, method, etc.
- The significance of the special __init__ method
- Data Abstraction, Data Encapsulation, and Information Hiding
- Properties, the difference between an attribute and a property
- The Pythonic way to write getters and setters
- Special __str__ and __repr__ methods
- Class attributes, object attributes, class methods, and static methods
- Dynamically creating arbitrary new attributes for existing instances
- Binding attributes to objects and classes
- __dict__ of a class and an instance of a class
- How Python finds the attributes of an object or class
- Using the getattr function

### Copyright - Plagiarism
- Solutions should be unique to meet learning objectives
- No content of this project should be published
- Any form of plagiarism is strictly forbidden

### Requirements
- Editors: vi, vim, emacs
- Code interpretation/compilation: Ubuntu 20.04 LTS using Python 3.8.5
- Files end with a new line
- First line of all files: `#!/usr/bin/python3`
- Mandatory README.md file at the root of the project folder
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- Length of files will be tested using wc

## Tasks

### Task 0: Simple Rectangle
- Write an empty class Rectangle that defines a rectangle.
- No import of any module is allowed.

### Task 1: Real Definition of a Rectangle
- Write a class Rectangle with private instance attributes `width` and `height`.
- Implement width and height as properties with getters and setters.
- Instantiation with optional width and height is allowed.

### Task 2: Area and Perimeter
- Enhance the Rectangle class to include methods for calculating area and perimeter.
- Implement properties for width and height with getters and setters.

### Task 3: String Representation
- Improve the Rectangle class to include a string representation.
- Print and str should display the rectangle using `#` characters.
- Implement width and height properties with getters and setters.

### Task 4: Eval is Magic
- Implement the `__repr__` method for the Rectangle class.
- Ensure that the representation can be used to recreate a new instance with eval().

### Task 5: Detect Instance Deletion
- Print a message when an instance of Rectangle is deleted.

### Task 6: How Many Instances
- Add a class attribute `number_of_instances` to count instances of Rectangle.
- Increment during new instance instantiation and decrement during instance deletion.

### Task 7: Change Representation
- Add a class attribute `print_symbol` to the Rectangle class for string representation.
- The symbol can be any type.
- Print and str methods should use this symbol.

### Task 8: Compare Rectangles
- Add a static method `bigger_or_equal` to Rectangle class.
- Return the rectangle with the larger area.
- Raise TypeError if arguments are not instances of Rectangle.

### Task 9: A Square is a Rectangle
- Enhance the Rectangle class to include a class method for creating squares.
- The square method should return a new Rectangle instance with equal width and height.

---

**Copyright © 2024 ALX, All rights reserved.**
