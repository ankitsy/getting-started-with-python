'''
Dictionaries are another example of a data structure.
A dictionary is used to map or associate things you want to store the keys you need to get them.
A dictionary in Python is just like a dictionary in the real world.
Python Dictionary are defined into two elements Keys and Values.

    Keys: will be a single element
    Values: can be a list or list within a list, numbers, etc.
'''

monthConversions = {
    'Jan' : 'January',
    'Feb' : 'February',
    'Mar' : 'March',
    'Apr' : 'April',
    'May' : 'May',
    'Jun' : 'June',
    'Jul' : 'July',
    'Aug' : 'August',
    'Sep' : 'September',
    'Oct' : 'October',
    'Nov' : 'November',
    'Dec' : 'December'
}
# Two methods to access a specific or value:
print(monthConversions['Nov'])
print(monthConversions.get('Dec'))

# Incase we enter wrong key which are not mapped we can use pass a default value like below:
print(monthConversions.get('Luv', 'Not a Valid Key'))

# We can assign variable like:
x = monthConversions['Apr']
print(x)

# We can change a value in a dictionary like:
monthConversions['Apr'] = 'Love'
print(monthConversions['Apr']) # It will output Love for key 'Apr'

# We can loop through a dictionary like:
for m in monthConversions:
    print(monthConversions[m])
# OR

for m in monthConversions.values():
    print(m)

# OR we can print both keys and values in a dict like:
for k, v in monthConversions.items():
    print(k, v)
