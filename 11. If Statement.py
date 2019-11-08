'''
I wake up
If I'm hungry
    I eat breakfast

If leave my house
if it's cloudy'
    I bring an umbrella
otherwise
    I bring sunglasses

Im at a restaurant
if I want meat
    I order a steak
otherwise if I want pasta
    I order spaghetti
otherwise
    I order Salad
'''

is_male = False  # We create boolean variable storing weather a person is male
is_tall = False
if is_male or is_tall:
    print('You are a male or tall!')
else:
    print('You are neither male nor tall!')  # if is_male is False


is_male = False
is_tall = False
if is_male and is_tall:
    print('You are a male and tall!')
else:
    print('You are either not male or not tall or both')  # if is_male is False

# we can play with True False values for different results
is_male = False
is_tall = True
if is_male and is_tall:
    print('You are a male and tall!')
elif is_male and not(is_tall):
    print('You are a short male')
elif not(is_male) and is_tall:
    print('You are a not a male but are tall')
else:
    print('You are not a male and not tall')