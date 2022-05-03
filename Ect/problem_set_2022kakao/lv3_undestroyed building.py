import numpy as np


def solution1(board, skill):
    # t10, e0, 53.8점 기본 해
    answer = 0

    for s in skill:
        degree = -s[5] if s[0] == 1 else s[5]

        for r in range(s[1], s[3] + 1):
            for c in range(s[2], s[4] + 1):
                board[r][c] += degree

    for line in board:
        for l in line:
            if l > 0:
                answer += 1
    return answer


def solution2(board, skill):
    # t10, e0, 53.8점
    answer = 0
    row = len(board)
    col = len(board[0])
    board = np.array(board)

    for s in skill:
        print("=====")
        print(board)
        dmg_brd = np.zeros((row, col), dtype='int32')
        degree = -s[5] if s[0] == 1 else s[5]
        r1, c1 = s[1], s[2]
        r2, c2 = s[3], s[4]

        dmg_brd[r1][c1] += degree
        if r2 + 1 < row:
            dmg_brd[r2 + 1][c1] += -degree
            if c2 + 1 < col:
                dmg_brd[r2 + 1][c2 + 1] += degree
        if c2 + 1 < col:
            dmg_brd[r1][c2 + 1] += -degree

        dmg_brd = dmg_brd.cumsum(axis=1)
        dmg_brd = dmg_brd.cumsum(axis=0)
        board = board + dmg_brd

    for val in board.reshape(-1):
        if val > 0:
            answer += 1
    return answer


def solution3(board, skill):
    # t10, e7, max_t 3.30ms, max_e 2924.58ms
    answer = 0
    row = len(board)
    col = len(board[0])
    board = np.array(board)

    dmg_brd = np.zeros((row, col), dtype='int32')
    for s in skill:
        degree = -s[5] if s[0] == 1 else s[5]
        r1, c1 = s[1], s[2]
        r2, c2 = s[3], s[4]

        dmg_brd[r1][c1] += degree
        if r2 + 1 < row:
            dmg_brd[r2 + 1][c1] += -degree
            if c2 + 1 < col:
                dmg_brd[r2 + 1][c2 + 1] += degree
        if c2 + 1 < col:
            dmg_brd[r1][c2 + 1] += -degree

    dmg_brd = dmg_brd.cumsum(axis=1)
    dmg_brd = dmg_brd.cumsum(axis=0)
    board = board + dmg_brd

    for val in board.reshape(-1):
        if val > 0:
            answer += 1
    return answer
