'''
Python has some main data types like Strings, Numbers, Booleans, etc.
And it has data structures like lists, tuples, dictionaries and sets to store data types mentioned above.
But in real world not everything can be defined using strings or numbers or booleans in lists or tuples, etc.
For storing data which can't be stored in data structures or defined in data types. We create Class.

Clas:
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
For the class we will create below, class is basically what defines a student. And the actual student is the Object

__init__() function is used to assign values to object properties, or other operations that are
necessary to do when the object is being created
'''

# For 25. Clauses and Objects:
class Student:  # within class we can define attributes about students. A class is basically defining what a student is.
   def __init__(self, name, major, gpa, is_on_probation):  # these are the parameters we passed for the students. In the other file, where we passed: Ankit, Business, 3.3, False are gonna be stored in these parameters.
      self.name = name  # self is referring to the actual Student object that we create in the other file(student1,etc.)
      self.major = major  # it means: the major of the student is gonna be equal to the major we passed in above
      self.gpa = gpa
      self.is_on_probation = is_on_probation

