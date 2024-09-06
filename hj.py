def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")

        row, col = -1, -1
        while row not in range(3) or col not in range(3) or board[row][col] != ' ':
            try:
                row, col = map(int, input("Enter row and column (0, 1, or 2) separated by space: ").split())
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space.")

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = 1 - current_player


if __name__ == "__main__":
    tic_tac_toe()
