'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.

We use try except to avoid our program to break because of a error.
'''
try:
    number = int(input('Enter a number: '))
    print(number)
except:  # only using except is way too broad.
    print('Invalid input 1')

# In the below example, we only get the Invalid input, but we did not know from the except what caused that error and-
# -what is that error.
try:
    value = 10/0
    number = int(input('Enter a number: '))
    print(number)
except:
    print('Invalid input 2')

# We can create 2 different except blocks to catch 2 different error and store error as variable.
try:
    # value = 10 / 0
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisionError as err:  # We can store error in a variable, say err, to show the exact error text that occurs
    print(err)
except ValueError as err1:
    print(err1)
