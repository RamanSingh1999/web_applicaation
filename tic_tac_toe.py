def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")


def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def check_tie(board):
    return all(spot in ['X', 'O'] for spot in board)


def tic_tac_toe():
    board = [str(i + 1) for i in range(9)]  # Initialize board with numbers 1 to 9
    current_player = 'X'
    
    print("Tic-Tac-Toe Game!")
    print_board(board)
    
    while True:
        # Get the player's move
        move = input(f"Player {current_player}, enter a number (1-9): ")
        
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1  # Adjust for 0-indexed board
            if board[move] not in ['X', 'O']:  # Check if the spot is available
                board[move] = current_player
                print_board(board)
                
                if check_win(board, current_player):
                    print(f"Player {current_player} wins!")
                    break
                
                if check_tie(board):
                    print("It's a tie!")
                    break
                # Switch players
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("This spot is already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    tic_tac_toe()
