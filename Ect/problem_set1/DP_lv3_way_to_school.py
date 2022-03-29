def solution1(m, n, puddles):
    # 45점, t10, e0
    if m == 1 and n == 1:
        return 1
    elif [m, n] in puddles:
        return 0
    elif m == 1:
        return solution1(m, n-1, puddles)
    elif n == 1:
        return solution1(m-1, n, puddles)
    else:
        return solution1(m, n-1, puddles) + solution1(m-1, n, puddles)


def solution2(m, n, puiddles):
    # 75점, t7, e8
    t = [[1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] in puiddles:
                t[i][j] = 0
            else:
                if i == 0:
                    t[i][j] = 1
                elif j == 0:
                    t[i][j] = 1
                else:
                    t[i][j] = t[i - 1][j] + t[i][j - 1]

    return t[n - 1][m - 1] % 1000000007


def solution3(m, n, puiddles):
    # 100점, t10 max 0.12ms, e10 max 4.3ms
    # puiddles x, y 좌표가 반대인 악질 문제
    t = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] in puiddles:
                t[i][j] = 0
            else:
                if i == 0 and j == 0:
                    t[i][j] = 1
                elif i == 0:
                    t[i][j] = t[i][j - 1]
                elif j == 0:
                    t[i][j] = t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j] + t[i][j - 1]

    return t[n - 1][m - 1] % 1000000007


solution3(4, 3, [[2, 2]])