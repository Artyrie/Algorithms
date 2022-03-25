def solution(N, number):
    # 55.6점, t5
    MAX = 32000
    voca = [[False for _ in range(MAX + 1)], [False for _ in range(MAX + 1)]] # 0짝 1홀
    voca[1][N] = True
    cnt = 1
    while cnt < 8:
        if voca[0][number] or voca[1][number]:
            return cnt

        switch = abs(cnt % 2 - 1)
        for i in range(1, MAX):
            if not voca[cnt % 2][i]:
                continue
            voca[switch][abs(N - i)] = True
            if N % i == 0:
                voca[switch][int(N / i)] = True
            if i % N == 0:
                voca[switch][int(i / N)] = True
            if N * i < MAX:
                voca[switch][N * i] = True
            if N + i < MAX:
                voca[switch][N + i] = True
            if int(str(N) * (cnt + 1)) < MAX:
                voca[switch][int(str(N) * (cnt + 1))] = True

        cnt += 1

    return -1


def solution2(N, number):
    # 100점, t9 max 1371.75ms
    voca = {i:set([int(str(N) * i)]) for i in range(1, 9)}

    cnt = 1
    while True:
        if number in voca[cnt]:
            return cnt
        elif cnt >= 8:
            return -1

        for i in range(1, cnt + 1):
            for v1 in voca[i]:
                for v2 in voca[cnt + 1 - i]:
                    if v1 + v2 < 32000:
                        voca[cnt + 1] = voca[cnt + 1].union(set([v1 + v2]))
                    if v1 * v2 < 32000:
                        voca[cnt + 1] = voca[cnt + 1].union(set([v1 * v2]))
                    if v1 % v2 == 0:
                        voca[cnt + 1] = voca[cnt + 1].union(set([v1 // v2]))
                    if v2 % v1 == 0:
                        voca[cnt + 1] = voca[cnt + 1].union(set([v2 // v1]))
                    if abs(v1 - v2) != 0:
                        voca[cnt + 1] = voca[cnt + 1].union(set([abs(v1 - v2)]))
        cnt += 1


print(solution2(8, 53))