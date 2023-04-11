from colorama import Fore, Style
import shutil
from typing import Dict, List, Tuple


def color_boards(boards: List[List[List[str]]], symbol_color_dict: Dict[str, str]) -> str:
    """Returns a string representation of the boards with symbols colored according to the symbol_color_dict.

    Args:
        boards: A list of 2D lists, where each inner list represents a single board.
        symbol_color_dict: A dictionary that maps symbols to color codes.

    Returns:
        A string representation of the boards with symbols colored according to the symbol_color_dict.
    """

    # Determine the size of each board
    board_size = len(boards[0][0])

    # Determine the maximum number of columns that can fit on a single line
    max_cols = shutil.get_terminal_size().columns // (board_size * 2 + 2)

    # Initialize an empty list to hold the colored board rows
    colored_board_rows = []

    # Loop over each group of max_cols columns
    for col_group in range(0, len(boards[0]), max_cols):
        # Initialize an empty list to hold the colored rows of each board
        colored_rows = [[] for _ in range(board_size)]

        # Loop over each row of boards
        for row in boards:
            # Loop over each board in the current column group
            for board in row[col_group:col_group+max_cols]:
                # Loop over each row of the board
                for j, row in enumerate(board):
                    # Color the symbols in the row according to the symbol_color_dict
                    colored_row = [symbol_color_dict.get(
                        symbol, Fore.WHITE) + symbol + Style.RESET_ALL for symbol in row]
                    # Append the colored row to the list of colored rows
                    colored_rows[j].append(colored_row)

        # Loop over the colored rows and join them together into strings
        for i, colored_row in enumerate(colored_rows):
            colored_board_row = '  '.join(
                [''.join(row) for row in colored_row])
            # Append the colored board row to the list of colored board rows
            colored_board_rows.append(colored_board_row)

        # Append a blank line to separate the column groups
        colored_board_rows.append('')

    # Join the colored board rows together into a single string and return it
    return '\n'.join(colored_board_rows)




if __name__ == "__main__":
    # Sample input data
    board1 = [['X', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'X']]
    board2 = [['O', 'X', 'O'], ['X', 'O', 'O'], ['O', 'O', 'X']]
    board3 = [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
    boards = ((board1, board2), (board3,))

    symbol_color_dict = {
        'X': Fore.RED,
        'O': Fore.BLUE
    }

    # Call the function to get the colored boards as a string
    colored_boards = color_boards(boards, symbol_color_dict)

    # Print the colored boards to the terminal
    print(colored_boards)
