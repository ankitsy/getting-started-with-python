# Tut1: Print Hello
print("Hello World")

# Tut2: Drawing a Shape:
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /____|")

# Tut3: Variables and Data Types
'''
Variables: are containers for storing data values. A variable is created the moment you first assign a value to it.
Unlike other programming languages, Python has no command for declaring a variable.

String variables: can be declared either by using single or double quotes:
Data types: Every value in Python has a datatype. Different data types in Python are Numbers, List, Tuple, Strings, Dictionary, etc. 
Boolean Values: Boolean values are the two constant objects False and True. 
'''
# We can create variables storing the string variables which we can use in further code.
character_name = 'Ram'
character_age = 65.5 # This data type is numbers. It can be in decimals too.

print('There was a man named ' + character_name + ',')
print('He was ' + character_age + ' years old.')
print('He really liked the name ' + character_name + ',')
print('But did not like being ' + character_age + '.\n')

# We can also change the variable value midway like this:
print('There was a man named ' + character_name + ',')
print('He was ' + character_age + ' years old.')
character_name = 'Shayam' # character name is changed so the next line of codes will use this updated value
print('He really liked the name ' + character_name + ',')
print('But did not like being ' + character_age + '.')

