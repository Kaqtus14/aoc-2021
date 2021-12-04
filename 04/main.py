import sys
import pprint


def check_win(board):
    for x in range(len(board)):
        if all([n == -1 for n in board[x]]):
            return True

    for y in range(len(board)):
        if all([board[x][y] == -1 for x in range(len(board))]):
            return True

    return False


def sum_board(board):
    ret = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] != -1:
                ret += board[x][y]
    return ret


def replace_in_board(board, n):
    for x in range(5):
        for y in range(5):
            if board[x][y] == n:
                board[x][y] = -1
    return board


def parse_boards():
    with open("input.txt") as f:
        numbers = [int(x) for x in f.readline().strip().split(",")]
        boards = f.read().replace("  ", " ").split("\n\n")

    boards = [[[int(x) for x in line.split(" ") if x] for line in board.split("\n") if line] for board in boards]
    return numbers, boards


numbers, boards = parse_boards()
for n in numbers:
    for i in range(len(boards)):
        boards[i] = replace_in_board(boards[i], n)

        if check_win(boards[i]):
            pprint.pprint(boards[i])
            print(sum_board(boards[i]) * n)
            sys.exit(0)
