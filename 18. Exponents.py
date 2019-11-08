print(2**3)

# We will make a function for using exponents:
def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 3))
print(raise_to_power(4, 2))
print(raise_to_power(2, 10))
