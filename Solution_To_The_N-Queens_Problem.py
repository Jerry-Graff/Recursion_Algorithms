"""
N-QUEEEN PROBLEM: Place N-Queens on a N*N chessboard so that no queen
                  can attack each other.

Disclaimer: This program solves the N-Queens problem using a recursive
            backtracking algorithm. It has a time complexity of O(N!)
            and a space complexity of O(N^2). Please be aware:

Time Complexity: The time required to find solutions grows exponentially
                 with the size of the board (N). For larger boards, such
                 as N > 12, the computation time can become significant
                 and may take hours or more.

Space Complexity: The program uses additional memory proportional to N^2
                  to store the chessboard configuration.
"""


class NQueens:

    def __init__(self, n):
        self.n = n
        self.board = [["." for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check this col on upper side
        for i in range(row):
            if self.board[i][col] == "Q":
                return False
        # Check upper diagonal left
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == "Q":
                return False
        # Check upper diagonal right
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == "Q":
                return False

        return True

    def solve(self, row=0):
        # Base Case
        if row >= self.n:
            self.solutions.append(["".join(row) for row in self.board])
            return
        # Recursive Case: Places a queen in every col or current rowcd
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = "Q"
                self.solve(row+1)  # Recursion
                self.board[row][col] = "."

    def get_solutions(self):
        self.solve()
        return self.solutions


class Solutions:

    def __init__(self, solution):
        self.solution = solution

    def print_solutions(self):
        for index, solution in enumerate(self.solution, start=1):
            print(f"solution Number: {index}")
            for row in solution:
                print(row)
            print()


def main():
    while True:
        print("""
N-QUEENS PROBLEM: Place N-Queens on an N*N chessboard so that no queen
                  can attack each other.

    1. Find Solutions to the N-Queens Problem
    0. Exit program
        """)
        user_input = input(": ")
        if user_input == "1":
            n = int(input("Enter the size of the board (N*N): "))
            n_queens_solver = NQueens(n)
            solutions = n_queens_solver.get_solutions()
            solutions_printer = Solutions(solutions)
            print(f"Number of solutions for {n}-Queens: {len(solutions)}")
            solutions_printer.print_solutions()
        elif user_input == "0":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
