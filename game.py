# 2048-Game-Python    

import random
import os

# Function to initialize the grid
def initialize_grid():
    return [[0]*4 for _ in range(4)]

# Function to add a new 2 or 4 to the grid
def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

# Function to print the grid
def print_grid(grid):
    os.system('clear')
    print("2048")
    print("---------------------")
    for row in grid:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("{:4}".format(" "), end="")
            else:
                print("{:4}".format(cell), end="")
        print("|")
    print("---------------------")

# Function to move tiles left
def move_left(grid):
    for i in range(4):
        row = [cell for cell in grid[i] if cell != 0]
        row += [0] * (4 - len(row))
        for j in range(3):
            if row[j] == row[j + 1]:
                row[j] *= 2
                row[j + 1] = 0
        row = [cell for cell in row if cell != 0]
        row += [0] * (4 - len(row))
        grid[i] = row

# Function to move tiles right
def move_right(grid):
    for i in range(4):
        row = [cell for cell in grid[i] if cell != 0]
        row = [0] * (4 - len(row)) + row
        for j in range(3, 0, -1):
            if row[j] == row[j - 1]:
                row[j] *= 2
                row[j - 1] = 0
        row = [cell for cell in row if cell != 0]
        row = [0] * (4 - len(row)) + row
        grid[i] = row

# Function to move tiles up
def move_up(grid):
    for j in range(4):
        col = [grid[i][j] for i in range(4) if grid[i][j] != 0]
        col += [0] * (4 - len(col))
        for i in range(3):
            if col[i] == col[i + 1]:
                col[i] *= 2
                col[i + 1] = 0
        col = [cell for cell in col if cell != 0]
        col += [0] * (4 - len(col))
        for i in range(4):
            grid[i][j] = col[i]

# Function to move tiles down
def move_down(grid):
    for j in range(4):
        col = [grid[i][j] for i in range(4) if grid[i][j] != 0]
        col = [0] * (4 - len(col)) + col
        for i in range(3, 0, -1):
            if col[i] == col[i - 1]:
                col[i] *= 2
                col[i - 1] = 0
        col = [cell for cell in col if cell != 0]
        col = [0] * (4 - len(col)) + col
        for i in range(4):
            grid[i][j] = col[i]

# Function to check if the game is over
def is_game_over(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    return True

# Main function to run the game
def main():
    grid = initialize_grid()
    add_new_tile(grid)
    add_new_tile(grid)
    print_grid(grid)
    while not is_game_over(grid):
        move = input("Enter move (W/A/S/D): ").upper()
        if move == 'W':
            move_up(grid)
        elif move == 'A':
            move_left(grid)
        elif move == 'S':
            move_down(grid)
        elif move == 'D':
            move_right(grid)
        else:
            print("Invalid move! Please enter W/A/S/D.")
            continue
        add_new_tile(grid)
        print_grid(grid)
    print("Game Over!")

# Run the game
if __name__ == "__main__":
    main()
