
"""The module checks if a playing field is ready for
beginning a game.
"""

def stars_amount_counter(board: list) -> int:
    """Counts amount of stars in the given board.
    >>> stars_amount_counter(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
    "7    9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2 9****"])
    36
    """

    stars = 0

    for i in range(9):

        for j in range(9):

            if board[i][j] == '*':
                stars += 1

    return stars


def stars_and_color_presence_checker(board: list) -> bool:
    """Checks if color blocks have same numbers and if stars and
    ziros are in cells, in which they shouldn't be. Returns ture if
    anything wrong is found.
    >>> stars_and_color_presence_checker(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
    "7    9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2 9****"])
    False
    """

    for i in range(5):
        color_block = {}

        for j in range(4 - i, 9 - i):

            if board[j][i] == '*' or board[j][i] == '0':
                return True

            if board[j][i] != ' ':
                color_block[board[j][i]] = color_block.setdefault(
                    board[j][i], 0) + 1

        for j in range(i + 1, i + 5):

            if board[8 - i][j] == '*' or board[8 - i][j] == '0':
                return True

            if board[8 - i][j] != ' ':
                color_block[board[8 - i][j]
                            ] = color_block.setdefault(board[8 - i][j], 0) + 1

        for value in color_block.values():

            if value > 1:
                return True

    return False


def validate_board(board: list) -> bool:
    """Checks if rows and strings have same numbers and
    calls stars_amount_counter to check if amount of stars is 36
    as it should be and stars_and_color_presence_checker to check if
    all is right with color blocks. Returns False if anything is against
    the rules.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
    "7    9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2 9****"])
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
    "7    9 5 ", " 6  83  *", "3   2  **", "2 8  2***", "  2 9****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
    "7    9 5 ", " 6  83  *", "3 0 2  **", "  8  2***", "  2 9****"])
    False
    """

    for i in range(9):
        string = {}
        row = {}

        for j in range(9):

            if board[i][j] != '*' and board[i][j] != ' ':
                string[board[i][j]] = string.setdefault(board[i][j], 0) + 1

            if board[j][i] != '*' and board[j][i] != ' ':
                row[board[j][i]] = row.setdefault(board[j][i], 0) + 1

        for j in string.values():

            if j > 1:
                return False

        for j in row.values():

            if j > 1:
                return False

    if stars_amount_counter(board) != 36 or stars_and_color_presence_checker(board):
        return False

    return True


# print(validate_board([
#     "**** ****",
#     "***1 ****",
#     "**  3****",
#     "* 4 1****",
#     "7    9 5 ",
#     " 6  83  *",
#     "3   2  **",
#     "  8  2***",
#     "  2 9****"
# ]))

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
