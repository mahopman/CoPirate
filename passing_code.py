# Here is tic tac toe code that passes the test cases
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column): ")
            row, col = map(int, move.split())
            return row - 1, col - 1
        except ValueError:
            print("Invalid input. Please enter row and column as two numbers separated by a space.")

def is_valid_move(board, move):
    row, col = move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves_made = 0

    while True:
        print_board(board)
        move = get_move(current_player)

        if not is_valid_move(board, move):
            print("Invalid move. Try again.")
            continue

        row, col = move
        board[row][col] = current_player
        moves_made += 1

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif moves_made == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
