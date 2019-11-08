num1 = float(input('Enter first number: ')) # using float() here means as soon as the user inputs a number it will be converted to number instead of a string type
op = input('Enter operator: ')
num2 = float(input('Enter second number: '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
        print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print('Invalid Operator! Enter a valid operator.')

