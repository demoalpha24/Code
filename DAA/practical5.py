def is_safe(board, row, col, n):
    # Check if there's a queen in the same row
    for i in range(n):
        if board[row][i] == 1:
            return False

    # Check if there's a queen in the same column
    for i in range(n):
        if board[i][col] == 1:
            return False

    # Check for a queen on the top-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for a queen on the top-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # It's safe to place a queen at (row, col)
    return True


def backtrack(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if backtrack(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack
    return False


def main():
    n = int(input("Enter the size of the chessboard: "))
    board = [[0 for _ in range(n)] for _ in range(n)]

    if backtrack(board, 0, n):
        # Print the first solution found
        for row in board:
            for cell in row:
                if cell == 0:
                    print("_ ", end=" ")
                else:
                    print("Q ", end=" ")
            print()
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
