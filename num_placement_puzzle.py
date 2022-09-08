from array import array
import random


def create_board(n: int) -> array:
    """Input the number of equalities you would like on your board"""

    n *= 2
    n += 1
    board = [float("inf")] * n

    for i in range(1, n, 2):
        if random.randint(0, 1):
            board[i] = "<"

        else:
            board[i] = ">"

    return board


def is_greater_than_symb(arr: array, ind: int) -> bool:
    """Check if the symbol is < or >"""

    if arr[ind] == ">":
        return True

    return False


def min_(arr: array) -> int:
    """Returns the minimum num of the input array and removes it"""
    num = min(arr)
    arr.remove(num)
    return num


def max_(arr: array) -> int:
    """Returns the max num of the input array and removes it"""
    num = max(arr)
    arr.remove(num)
    return num


def fill_board(board: array, num_arr: array) -> None:
    """Fills the given board with the numbers in num_arr in a logical way"""

    for symb_ind in range(1, len(board) - 1, 2):
        num_ind = symb_ind - 1

        if is_greater_than_symb(board, symb_ind):
            board[num_ind] = max_(num_arr)

        else:
            board[num_ind] = min_(num_arr)

    if is_greater_than_symb(board, symb_ind):
        board[num_ind + 2] = max_(num_arr)

    else:
        board[num_ind + 2] = min_(num_arr)


def solve_puzzle(board: array, num_arr: array) -> str:
    """Returns the board if the puzzle is solvable, and False if not"""

    fill_board(board, num_arr)

    for symb_ind in range(1, len(board) - 1, 2):
        num_ind = symb_ind - 1

        if is_greater_than_symb(board, symb_ind):
            if board[num_ind] < board[num_ind + 2]:
                return "False"

        else:
            if board[num_ind] > board[num_ind + 2]:
                return "False"

    return f"Solved board: {board}"


board = create_board(8)
print(solve_puzzle(board, [1, 7, 3, 4, 12, 5, 0, 15, 8, 6]))
