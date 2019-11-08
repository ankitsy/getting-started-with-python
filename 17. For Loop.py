'''
ForLoop:
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

'''

# For loop in a String:
for l in 'Ankit is cool':  # Instead of l, you can write anything. It is called a variable here. It is spoken as for each variable i.e letter/ string/ element in 'Ankit is cool'
    print(l) # print that variable

# Array: Arrays are used to store multiple values in one single variable. Unlike lists, in Numpy array all the
# elements of the list are of the same type.

# For loop in a array:
friends = ['Ankit', 'Ram', 'Shayam', 'Dholu']
for friend in friends:
    print(friend)

# For loop in Numbers:
for i in range(1,10):
    print(i)

# For loop in array using indexing: it will also print friends but ussing different approach
friends = ['Ankit', 'Ram', 'Shayam', 'Dholu']
for index in range(len(friends)):  # len(friends) will give 3.
    print(friends[index])

#
for i in range(3):
    if i == 0:
        print('first iteration')
    else:
        print('other iteration')
