import chess
import chess.pgn


# 4 spaces for indentation
INDENT_STR = ' ' * 4


SQUARE_WHITE = '◽'
SQUARE_BLACK = '◾'


def get_background_color(row: int, col: int) -> str:
    if (row % 2 + col % 2) % 2 == 1:
        return SQUARE_BLACK
    else:
        return SQUARE_WHITE


def show_board(board: chess.Board, indent: str):
    for row in range(7, -1, -1):
        print(f'{indent}print("', end='')
        for col in range(8):
            square = chess.square(col, row)
            piece = board.piece_at(square)
            if piece is None:
                # Just show the background color
                print(f'{get_background_color(row, col)}', end='')
            else:
                print(f'{piece.symbol()} ', end='')

        # End of row
        print('")')


def recursive_generate(depth_remaining: int, board: chess.Board):
    print()
    indent = INDENT_STR * len(board.move_stack)
    indent_if = INDENT_STR * (len(board.move_stack) + 1)
    # If there is no more recursion required, give an error message
    # We can manually expand on required branches later
    if depth_remaining == 0:
        print(
            f'{indent}print("ERROR: this position has not been generated yet! '
            f'Please open an issue on the project GitHub page.")'
        )
        print(f'{indent}exit(1)')
        return

    # As player for their move
    whose_turn = 'Your' if board.turn == chess.WHITE else 'Opponent\'s'
    print(f'{indent}print("{whose_turn} turn! {board.fullmove_number}.")')
    print(f"{indent}player = input()")
    print()

    legal_moves = board.legal_moves
    # If there are none, we should tell the user what the outcome of the game
    # was
    if legal_moves.count() == 0:
        ...
        # TODO

    first_if = True
    # Otherwise for every possible response
    for move in board.legal_moves:
        iffy = 'if' if first_if else 'elif'
        # Add the if statement and make the move
        print(f'{indent}{iffy} player == "{board.san_and_push(move)}":')

        # Show the state of the board
        show_board(board, indent_if)

        # Recurse to generate more moves
        recursive_generate(depth_remaining - 1, board)

        # Unmake move
        board.pop()


def generate(depth: int):
    # Set up initial board
    board = chess.Board()
    # Print it
    print('print("Welcome to chess!")')
    print('print()')
    print()
    show_board(board, '')
    # And recurse
    recursive_generate(depth, board)
