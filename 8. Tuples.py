'''
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses,
whereas lists use square brackets.
Tuple are immutable: meaning it can not change or modified

'''

coordinates = (4,5)
print((coordinates[0]))  # we can access tuples using indexing, just like lists
# But we cannot modify a tuple. We use tuple data we know is never going to change.
# coordinates[0] = 3  # it will give error, as we cannot change a tuple

# We can store tuples in a list.
coordinates = [(4,5), (9,32), (55,88), (2,43)]
coordinates[0] = (1,2) # entire tuple can be changed in a list, but values inside a tuple can never be modified
print(coordinates)
