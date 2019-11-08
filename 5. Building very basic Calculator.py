'''
We will get 2 numbers from user and store it in variable and build a very basic calculator

'''
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
result = num1 + num2
print(result) # if the user had inputs 5 and 4, the result will show 54 because pythin thinks of them as strings. So we change the inputs to Number first.

# To convert the String into Number there are 2 methods: int() which is used for Integers; another is float() which takes decimal values too.
result = float(num1) + float(num2)
print(result)