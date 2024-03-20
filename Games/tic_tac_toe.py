#!/usr/bin/python3

# Function to initialize the game board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the game board
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to get player move
def get_move():
    while True:
        try:
            row = int(input("Enter row number (0, 1, 2): "))
            col = int(input("Enter column number (0, 1, 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input! Row and column numbers should be between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter integers.")

# Function to update the board with the player's move
def update_board(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("That position is already taken!")
        return False

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check for a draw
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Main function to run the game
def tic_tac_toe():
    board = initialize_board()
    current_player = 'X'

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")
        row, col = get_move()

        if update_board(board, row, col, current_player):
            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
