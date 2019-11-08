# Creating StudentX class for using in the 27. Object Function

class StudentX:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honors(self):  # Here we created a function inside the class for finding out if a student is honors or not
        if self.gpa > 3.5:
            return True
        else:
            return False


