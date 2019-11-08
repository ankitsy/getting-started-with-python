# Refer to the StudentClass.py file before reading this file.
from StudentClass import Student

student1 = Student('Ankit', 'Business', 3.3, False)  # Here we created a student1, which is an object in Student class.
student2 = Student('Ram', 'Finance', 3.8, True)
print(student1.gpa)  # We can print information about the students like this
print(student1.is_on_probation)