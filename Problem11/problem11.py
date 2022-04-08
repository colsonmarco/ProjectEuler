import os
import numpy as np

# Question can be found at https://projecteuler.net/problem=11

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
grid = np.empty((0,20), str)
max_prod = 0

file = open(os.path.join(__location__, "grid.txt"))

for line in file:
    line = line.replace('\n', '')
    grid = np.vstack([grid, [line.split(" ")]])
file.close()

for row in grid:
    for i in range(len(row) - 4):
        max_prod = max(max_prod, int(row[i]) * int(row[i+1]) * int(row[i+2]) * int(row[i+3]))
for column in grid.T:
    for i in range(len(column) - 4):
        max_prod = max(max_prod, int(column[i]) * int(column[i+1]) * int(column[i+2]) * int(column[i+3]))
for i in range(16):
    for j in range(16):
        max_prod = max(max_prod, int(grid[i,j]) * int(grid[i+1,j+1]) * int(grid[i+2,j+2]) * int(grid[i+3,j+3]))
for i in range(3, 20):
    for j in range(16):
        max_prod = max(max_prod, int(grid[i,j]) * int(grid[i-1,j+1]) * int(grid[i-2,j+2]) * int(grid[i-3,j+3]))
print(max_prod)