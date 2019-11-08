'''
We can read files from external sources.
'''

employee_file = open('employee.txt', 'r')
# r means read mode
# w means write mode
# a means append mode
# r+ means read and write mode

# We can use various functions in this employee file
print(employee_file.readable())  # to check if the file is readable. It will return a True or False value
# print(employee_file.read())  # it will read all the information in the file
# print(employee_file.readline())  # it will read the first line
# print(employee_file.readline())  # if we repeat this function, it will read the second line and so on
# print(employee_file.readlines()) # it will rea lines in an array form
# print(employee_file.readlines()[1]) # using indexing it will read the line at index 1.

for employee in employee_file.readlines():  # for loop for reading multiple lines at once
    print(employee)

employee_file.close()  # open file should be closed when work is done. It is a good practice.