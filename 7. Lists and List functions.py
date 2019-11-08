'''
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

Below notes are for Lists.
'''
friends = ['Kevin', 'Ankit', '1', False]
# Lists can store anything- Strings, Numbers, or Booleans. List is always in square parenthesis
print(friends)
print(friends[0]) # We can access any value from a list using indexing, indexing starts from 0 in a list. 0 will print Kevin, 1 will print Ankit.
print(friends[-1]) # Using negative in index will start from the end of the list. Last element is -1, 2nd last is -2 and so on. THERE IS NO -0.
print(friends[1:]) # Using Range in indexing, we can select from a range of r=values in the list. [1:] means from 1 to the last value
print(friends[1:3]) # [1:3] means from 1 to 2. NOTE: IT DOES OT INCLUDE 3.
print(friends[:3]) # [:3] means from starting to 2. NOTE: IT DOES OT INCLUDE 3.

# Modifying values inside a list
friends[3] = 'Dholu'  # this will change the value at index 3 in friends list to Dholu
print(friends[3])

# List functions
lucky_number = [15,99,24,13,45,62]
friends = ['Ram', 'Dholu', 'Molu', 'Kalia', 'Shin', 'Chan']

# friends.extend(lucky_number) # extends() tterates over its argument and adding each element to the list and extending the list.
friends.append('Kalia')  # append() adds the element on to the end of the list
friends.insert(1, 'Bholu')  # insert() is used to insert a element at a specific position. List gets pushed to the right. Takes two parameters: index position and element to be inserted
friends.remove('Bholu')  # remove() removes the element mentioned inside this function.
# friends.clear() # removes all the elements inside the list
# friends.pop() # pop removes the last element off the list
# to find out if a particular element is in the list, use index like below:
print(friends.index('Dholu'))  # if a name is not in the list, it will give an error
print(friends.count('Kalia'))  # count() takes just 1 parameter. and it counts the total number of specified element in a list.
friends.sort()  # sorts the list in ascending/ alphabetical order
friends.reverse()  # reverses the order in the list
friends2 = friends.copy()  # copy() creates a copy of a list. We stored it in new list named friends2.

print(friends)
