from array import array

MOVE_N = None
MOVE_X = 0
MOVE_O = 1

WON_X = MOVE_X
WON_O = MOVE_O
WON_DRAW = 2

def check_winner(board: array) -> int:

    try:
        LOC_WIN_COMBINATION = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for combination in LOC_WIN_COMBINATION:
            a = board[combination[0]]
            b = board[combination[1]]
            c = board[combination[2]]

            # Check if combination is filled (accept only combination with moves)
            if all(move_val is not None for move_val in (a, b, c)):
                if (a == b) and (a == c):
                    winner = a
                    return winner  # Winner detected

        return MOVE_N  # No winner detected

    except Exception as e:

        return f"Error in check_winner : {e}"


def get_available_move(board: array) -> array:
    return [index for index, panel in enumerate(board) if panel is None]


def update_board(board: array, player: int, position: int) -> array:
    new_board = board[:]
    new_board[position] = player
    return new_board


def minimax(board: array, player: int):

    winner = check_winner(board)

    if winner == MOVE_X:
        return -1  # X Won
    elif winner == MOVE_O:
        return 1  # O Won
    elif not get_available_move(board):
        return 0  # Draw

    if player == MOVE_O:
        best_score = -float("inf")
        for position in get_available_move(board):
            new_board = update_board(board, MOVE_O, position)
            score = minimax(new_board, MOVE_X)
            best_score = max(best_score, score)
        return best_score

    if player == MOVE_X:
        best_score = float("inf")
        for position in get_available_move(board):
            new_board = update_board(board, MOVE_X, position)
            score = minimax(new_board, MOVE_O)
            best_score = min(best_score, score)
        return best_score


def get_best_move(board: array) -> int:
    best_score = -float("inf")
    best_move = -1

    for pos in get_available_move(board):
        score = minimax(update_board(board, MOVE_O, pos), MOVE_X)
        if score > best_score:
            best_score = score
            best_move = pos

    return best_move


def display(board: array):

    board = list(
        map(
            lambda x: "-" if x is None else "X" if x == 0 else "O" if x == 1 else x,
            board,
        )
    )

    print(f"[ {board[0]} ] [ {board[1]} ] [ {board[2]} ]")
    print(f"[ {board[3]} ] [ {board[4]} ] [ {board[5]} ]")
    print(f"[ {board[6]} ] [ {board[7]} ] [ {board[8]} ]")
    print(f"~*~*~*~")
