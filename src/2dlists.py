# creating list

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0]) # give index of row and column 

# using for loop

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for row in number_grid: # nested for loop
    for col in row:
        print(col)
