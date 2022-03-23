def solution(n, computers):
    # 100점, t13, max 1.02ms
    answer = 0
    com = [[j + 1 if computers[i][j] == 1 else 0 for j in range(n)] for i in range(n)]

    while com:
        net = set(com.pop())

        for _ in range(n * 2):
            if not com:
                break
            tmp = set(com.pop())
            if net.intersection(tmp) != {0}:
                net = net.union(tmp)
            else:
                com.insert(0, tmp)

        answer += 1
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])