#!/usr/bin/python3

def print_board(board):
    """Prints the Tic Tac Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner"""
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal (top-left to bottom-right) for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check diagonal (top-right to bottom-left) for a win
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """Check if the game is a draw (board is full and no winner)"""
    for row in board:
        if " " in row:  # If there's any empty space, it's not a draw yet
            return False
    return True

def tic_tac_toe():
    """Main game loop for Tic Tac Toe"""
    board = [[" "]*3 for _ in range(3)]  # Create a 3x3 empty board
    player = "X"  # X starts the game
    while True:
        print_board(board)
        # Get user input for row and column
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            # Check if input is within bounds
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue
        
        # Check if the selected spot is empty
        if board[row][col] == " ":
            board[row][col] = player
            # Check if there is a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            # Check if the game is a draw
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            # Switch players
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

# Start the game
if __name__ == "__main__":
    tic_tac_toe()

