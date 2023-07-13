import chess
import chess.pgn


# 4 spaces for indentation
TAB = ' ' * 4


SQUARE_WHITE = '◽'
SQUARE_BLACK = '◾'


COLOR_NAMES = {
    chess.WHITE: 'White',
    chess.BLACK: 'Black',
}


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
    indent = TAB * len(board.move_stack)

    # If the game is finished, we should tell the user what the outcome was
    # Need to do this before the depth check, since otherwise the user will
    # get that error instead
    if board.is_game_over(claim_draw=True):
        print(f'{indent}print("Game over!")')
        if board.is_checkmate():
            winner = not board.turn
            print(f'{indent}print("{COLOR_NAMES[winner]} wins by checkmate")')
        else:
            print(f'{indent}print("It\'s a draw!")')
        return

    # If there is no more recursion required, give an error message
    # We can manually expand on required branches later
    if depth_remaining == 0:
        print(
            f'{indent}print("ERROR: moves for this position have not been '
            f'generated yet! Please open an issue on the project GitHub '
            f'page.")'
        )
        print(f'{indent}exit(1)')
        return

    # As player for their move
    whose_turn = 'Your' if board.turn == chess.WHITE else 'Opponent\'s'
    print(f'{indent}print("{whose_turn} turn! {board.fullmove_number}.")')
    print(f"{indent}player = input()")
    print()

    first_if = True
    # Otherwise for every possible response
    for move in board.legal_moves:
        iffy = 'if' if first_if else 'elif'
        # Add the if statement and make the move
        print(f'{indent}{iffy} player == "{board.san_and_push(move)}":')

        # Show the state of the board
        show_board(board, indent + TAB)

        # Recurse to generate more moves
        recursive_generate(depth_remaining - 1, board)

        # Unmake move
        board.pop()
        first_if = False

    # Add a check for illegal inputs
    print(f'{indent}else:')
    print(f'{indent}    print("Illegal move!")')
    print(f'{indent}    exit(2)')


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
