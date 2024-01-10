def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '':
            return True

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False


def is_board_full(board):
    for row in board:
        if '' in row:
            return False
    return True


def play_game(agent_choice = False):
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    actions = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        if current_player == 'X':
            row = int(input(f"Player {current_player}, choose row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, choose column (0, 1, 2): "))
        else:
            row = actions[agent_choice][0]
            col = actions[agent_choice][1]

        if board[row][col] == '':
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")