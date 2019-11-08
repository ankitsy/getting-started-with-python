print(2.987)
print(-2) # Python can handle negative values just fine

# Mathematical equations
print(2 + 3)
print(3 * 4 + 5) # It will execute it serially answer will be 17
print(3 * (4 + 5)) # Python will first execute the equation inside the inner bracket then the remaining. Using brackets we can make very complex equations too.
print(10 % 3) # % is called Mod, which gives the Remainder of 10 divided by 3 as the output
print(10 / 3) # / is the normal divide

my_num = 5
print(my_num)
print(str(my_num)) # str() converts the specified value into a String.

# We cannot print Numbers alongside Strings, if they are of different data type, So we convert Number to String like below:
print(str(my_num) + ' is my lucky number.')

my_num=-5
print(abs(my_num)) # abs() function gives the absolute value of a number. For -5, abs will be 5.

print(pow(3,2)) #pow(val1, val2), pow function takes two parameters. Val1 is the just the number and Val2 is what power Val1 is to be raised to.
print(max(4,6,8)) # max() function can take n number of parameters and return the Max value. Similarly for min()
print(round(3.72)) # round() function rounds the value.

# To access a lot of other features using numbers, we import math module
from math import *

print(floor(300.11)) # floor() function in Python returns floor of x i.e., the largest integer not greater than x. Simple words, round the number UP.
print(floor(300.99))
print(floor(-1.11)) # it will give -2 which is the largest integer not greater than -1.11

print(ceil(300.11)) # ceil() in Python returns ceiling value of x i.e., the smallest integer not less than x. Simple words, round the number DOWN.
print(ceil(300.99))
print(ceil(-1.11)) # it will return -1 which is the smallest integer not less than -1.11

print(sqrt(36)) # sqrt() returns the square root of the number
