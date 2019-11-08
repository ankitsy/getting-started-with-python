# 2D list is Lists inside a list.
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0])  # it will print first element in number_grid which is a list
print(number_grid[0][0])  # it will give first element in the first list in the number_grid

for i in number_grid:  # it will print each list in the number_grid
    print(i)

# Nested For loop: means for loop inside a for loop like:
for i in number_grid: 
    for j in i:
        print(j)
