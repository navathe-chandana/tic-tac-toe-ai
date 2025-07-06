def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                moves.append((i, j))
    return moves

def evaluate(board):
    if check_winner(board, 'O'):
        return +1
    elif check_winner(board, 'X'):
        return -1
    else:
        return 0

def minimax(board, is_maximizing):
    if check_winner(board, 'O') or check_winner(board, 'X') or is_draw(board):
        return evaluate(board)

    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_available_moves(board):
            original = board[i][j]
            board[i][j] = 'O'
            score = minimax(board, False)
            board[i][j] = original
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_available_moves(board):
            original = board[i][j]
            board[i][j] = 'X'
            score = minimax(board, True)
            board[i][j] = original
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i, j in get_available_moves(board):
        original = board[i][j]
        board[i][j] = 'O'
        score = minimax(board, False)
        board[i][j] = original
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def main():
    board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            move = input(f"Player {current_player}, choose a position (1-9): ")
            valid = False
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = current_player
                        valid = True
            if not valid:
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is thinking...")
            i, j = best_move(board)
            board[i][j] = 'O'

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
5