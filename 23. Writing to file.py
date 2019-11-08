employee_file = open('employee.txt', 'a') # if we use w instead of a, it will overwrite the whole file
# employee_file.write('Toby - Human Resources')  # commented out as it will keep on appending with each run


# while appending you need to be very carefull, each time you run the code, it will add the same line again and again.
employee_file.write('\nKelly - Analyst')  # \n means it will append it in new line. these are called escape characters.
employee_file.close()

# To create a new file:
employee_file = open('employee1.txt', 'w')  # w is also used to create a new file, just change the name of the file
employee_file.write('\nKelly - Analyst')
employee_file.close()

# To create a new html page:
employee_file = open('sample.html', 'w')  # w is also used to create a new file, just change the name of the file
employee_file.write('<p> Hello World! This is HTML.</p>')
employee_file.close()



