import random as rd


def create_board(n):
    board = [float("inf")] * n

    for i in range(1,n,2):
        board[i] = lambda x: x if rd.rd.randint(0,1) == 1 x = "<"
    return board

print(create_board(10))