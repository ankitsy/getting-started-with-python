'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''

# In Python a function is defined using the def keyword. We will create a function which says Hi.


def say_hi():  # say_hi is just a name I gave to the function
    print('Hello User!')


say_hi()  # To call a function, use the function name followed by parenthesis.


def say_hi(name):  # we can pass parameters inside a function which means when the func is called, paramenters have to be provided.
    print('Hello ' + name + '!')  # We can access the parameter inside our function like shown


say_hi('Ankit')
say_hi('Ram')


def say_hi(name, age):  # multiple parameters can also be passed
    print('Hello ' + name + '!. You are ' + str(age)) # age is changed to string coz concatenation rule.


say_hi('Ankit', 22)
say_hi('Ram', 10)
