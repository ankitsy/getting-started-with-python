'''
Python has two primitive loop commands:
    1. while loops
    2. for loops
While loop: With the while loop we can execute a set of statements as long as a condition is true.
For loop: is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

While loop is explained through below code:
'''

i = 1
while i <= 10:  # anything we write below will keep on executing till i <= 10.
    print(i)  # this line will keep on executing in a loop until i becomes equal to 10.
    i += 1  # shorthand for means i=i+1
print('Done with loop')
