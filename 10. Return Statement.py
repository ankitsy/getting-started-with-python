'''
Return Statement:
The return keyword is to exit a function and return a value. Basically we provide a function information and-
- the function return the the output back using Return Statement.

In prev ex. we used print inside a func to say hi. But when when called it showed Hi User!.
But in cases where print is not used, we have to use return which will return the value whenever called.
'''


def cube(num):
    return num*num*num  # if we dont use return here it will show None when called.(ignore line below)
    print('Code') # it will not be executed as return ends the function whenever it is used.


print(cube(3))


result = cube(4) # we can also store it in a Variable
print(result)