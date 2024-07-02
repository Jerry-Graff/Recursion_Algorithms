# function solveMaze(maze):
#     # Determine dimensions of the maze
#     rows = length of maze
#     cols = length of maze[0] if rows > 0 else 0
    
#     # Initialize a solution matrix to store the path
#     solution = [[false for _ in range(cols)] for _ in range(rows)]
    
#     # Find the starting point 'S' in the maze
#     startRow, startCol = -1, -1
#     for r in range(rows):
#         for c in range(cols):
#             if maze[r][c] == 'S':
#                 startRow, startCol = r, c
#                 break
#         if startRow != -1:
#             break
    
#     # Find the finishing point 'F' in the maze
#     finishRow, finishCol = -1, -1
#     for r in range(rows):
#         for c in range(cols):
#             if maze[r][c] == 'F':
#                 finishRow, finishCol = r, c
#                 break
#         if finishRow != -1:
#             break
    
#     # Define directions for moving in the maze (up, down, left, right)
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
#     # Define a recursive function to find the path
#     def findPath(row, col):
#         # Base case: if current cell is the finishing point
#         if row == finishRow and col == finishCol:
#             solution[row][col] = true
#             return true
        
#         # Check if current cell is within bounds and is an open path
#         if 0 <= row < rows and 0 <= col < cols and maze[row][col] in [' ', 'F'] and not solution[row][col]:
#             # Mark current cell as part of the solution path
#             solution[row][col] = true
            
#             # Try all possible directions
#             for direction in directions:
#                 nextRow = row + direction[0]
#                 nextCol = col + direction[1]
                
#                 # Recursively check the next cell
#                 if findPath(nextRow, nextCol):
#                     return true
            
#             # If no direction leads to the solution, backtrack
#             solution[row][col] = false
#             return false
        
#         # Cell is either out of bounds, a wall, or already part of the solution path
#         return false
    
#     # Start searching for the path from the starting point
#     if startRow != -1 and startCol != -1:
#         findPath(startRow, startCol)
    
#     # Visualize the solution path in the maze
#     for r in range(rows):
#         for c in range(cols):
#             if solution[r][c]:
#                 print('O', end='')  # or any other visualization of the path
#             else:
#                 print(maze[r][c], end='')
#         print()  # newline after each row

# # Example maze representation (you can fill in your own maze)
# maze = [
#     ['S', ' ', 'X', ' ', ' '],
#     ['X', ' ', 'X', ' ', 'X'],
#     ['X', ' ', ' ', ' ', ' '],
#     ['X', 'X', 'X', ' ', 'X'],
#     [' ', ' ', ' ', ' ', 'F']
# ]

# solveMaze(maze)