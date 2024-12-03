import random

# Define the board and the winning combinations
board = [' ' for _ in range(9)]
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6)  # diagonals
]


# Function to print the game board
def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")
    print("\n")


# Check if a move is valid
def is_valid_move(move):
    return board[move] == ' '


# Check for a winner
def check_winner(player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


# Player makes a move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please choose a number between 1 and 9.")
            elif not is_valid_move(move):
                print("This space is already taken. Try again.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


# Computer makes a move
def computer_move():
    available_moves = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available_moves)
    board[move] = 'O'


# Check if the board is full (for a draw)
def is_board_full():
    return all(space != ' ' for space in board)


# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Player's turn
        player_move()
        print_board()
        if check_winner('X'):
            print("Congratulations! You win!")
            break
        if is_board_full():
            print("It's a draw!")
            break

        # Computer's turn
        computer_move()
        print_board()
        if check_winner('O'):
            print("Sorry, you lose! The computer wins.")
            break
        if is_board_full():
            print("It's a draw!")
            break


# Start the game
play_game()








