'''
Strigs: they contain plain text.
String literals in python are surrounded by either single quotation marks, or double quotation marks.

'''

print('Ankit\nAcademy') # \n inserts new line
print('Ankit\'s Academy') #\ only using backslash will make Python not read the word right next to it.

# CONCATENATION
phrase = 'Ankit Academy'
print(phrase + ' is cool') # this is Concatenation where a string is appended to string

# FUNCTIONS: We can use functions to modify the Strings but also to get information about the String.
print(phrase.lower()) # lower(), upper() function converts the string to lowercase/uppercase.
print(phrase.islower()) # islower(), isupper() gives boolean value if the String is lowercase or uppercase.
print(phrase.lower().islower()) # this will give True as the phrase was first converted to lowercase, then islower() is run.
print(len(phrase)) # len() gives the length of the string inside it
print(phrase[0]) # it will give the letter at position 0 from the phrase which is 'Ankit Academy'. A String get indexed at 0. So 0 position here is A.
# In programming giving information or value to a function, is called as 'passing a parameter'.
print(phrase.index('A'))# index() function will tell us where a specific character is located inside of our String. It only tells the location of first A it finds in the String.
print(phrase.index('Acad')) #this will tell the location from where 'Acad' started.
print(phrase.replace('Ankit', 'Ram')) # replace() function takes 2 parameters, first one which is to be replaced, second one with with it is to be replaced.






