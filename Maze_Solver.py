"""
Maze Solver Program

This program generates a random maze, solves it using a recursive backtracking
algorithm, and prints both the generated maze and the solvedmaze with the
solution path.

This code generates a different maze each time it is run and solves it,
displaying the initial and solved mazes with borders for clarity.

"""

import random


def generate_random_maze(rows, cols, wall_probability=0.3):
    # Create an empty maze filled with open paths
    maze = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Place random walls in the maze
    for r in range(rows):
        for c in range(cols):
            if random.random() < wall_probability:
                maze[r][c] = 'X'

    # Place the start ('S') and finish ('F') points
    start_row, start_col = random.randint(
        0, rows - 1), random.randint(0, cols - 1)
    finish_row, finish_col = random.randint(
        0, rows - 1), random.randint(0, cols - 1)

    # Ensure start and finish are not the same
    while finish_row == start_row and finish_col == start_col:
        finish_row, finish_col = random.randint(
            0, rows - 1), random.randint(0, cols - 1)

    maze[start_row][start_col] = 'S'
    maze[finish_row][finish_col] = 'F'

    return maze


def solve_maze(maze):
    # Determine dimensions of the maze
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0

    # Initialize a solution matrix to store the path
    solution = [[False for _ in range(cols)] for _ in range(rows)]

    # Find the starting point 'S' in the maze
    start_row, start_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start_row, start_col = r, c
                break
        if start_row != -1:
            break

    # Find the finishing point 'F' in the maze
    finish_row, finish_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "F":
                finish_row, finish_col = r, c
                break
        if finish_row != -1:
            break

    # Define directions for moving in the maze (up, down, left, right)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Define a recursive function to find the path
    def find_path(row, col):
        # Base case: if current cell is the finishing point
        if row == finish_row and col == finish_col:
            solution[row][col] = True
            return True

        # Check if current cell is within bounds and is an open path
        if 0 <= row < rows and 0 <= col < cols and maze[row][col] in [' ', 'F'] and not solution[row][col]:
            # Mark current cell as part of the solution path
            solution[row][col] = True

            # Try all possible directions
            for direction in directions:
                next_row = row + direction[0]
                next_col = col + direction[1]

                # Recursively check the next cell
                if find_path(next_row, next_col):
                    return True

            # If no direction leads to the solution, backtrack
            solution[row][col] = False
            return False

        # Cell is either out of bounds, a wall, or already part of the solution path
        return False

    # Start searching for the path from the starting point
    if start_row != -1 and start_col != -1:
        find_path(start_row, start_col)

    return solution


# Helper function to print the maze with borders and the solution path
def print_maze_with_solution(maze, solution):
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    print('+' + '-' * cols + '+')
    for r in range(rows):
        print('|', end='')
        for c in range(cols):
            if solution[r][c]:
                print('O', end=' ')  # Visualize the solution path
            else:
                print(maze[r][c], end='')
        print('|')
    print('+' + '-' * cols + '+')


# Example usage
rows, cols = 20, 20  # Dimensions of the maze
maze = generate_random_maze(rows, cols)
solution = solve_maze(maze)
print("Solved Maze:")
print_maze_with_solution(maze, solution)
