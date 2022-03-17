from collections import Counter


def solution(n, lost, reserve):
    # 70점, t14
    answer = 0
    tmp = [i + 1 for i in range(n)]
    clothes = Counter(tmp) - Counter(lost) + Counter(reserve)

    for i in range(1, n + 1):
        try:
            clothes[i] += 0
        except:
            clothes[i] = 0
        val = clothes[i]
        if val == 1:
            answer += 1
        elif val == 2:
            if i != 1 and clothes[i - 1] == 0:
                clothes[i - 1] += 1
                clothes[i] -= 1
                answer += 1
            elif clothes[i + 1] == 0:
                clothes[i + 1] += 1
                clothes[i] -= 1
                answer += 1
        else:
            if i != 1 and clothes[i - 1] == 2:
                clothes[i - 1] -= 1
                clothes[i] += 1
                answer += 1
            elif clothes[i + 1] == 2:
                clothes[i + 1] -= 1
                clothes[i] += 1
                answer += 1

    return answer


def solution2(n, lost, reserve):
    # 100점, t20, max 0.10ms
    answer = 0
    tmp = [i + 1 for i in range(n)]
    clothes = Counter(tmp) - Counter(lost) + Counter(reserve)

    for i in range(1, n + 1):
        try:
            clothes[i] += 0
        except:
            clothes[i] = 0
        val = clothes[i]
        if val == 1:
            answer += 1
        elif val == 2:
            if i > 1 and clothes[i - 1] == 0:
                clothes[i - 1] += 1
                clothes[i] -= 1
            elif i < n and clothes[i + 1] == 0:
                clothes[i + 1] += 1
                clothes[i] -= 1
            answer += 1
        else:
            if i > 1 and clothes[i - 1] == 2:
                clothes[i - 1] -= 1
                clothes[i] += 1
                answer += 1
            elif i < n and clothes[i + 1] == 2:
                clothes[i + 1] -= 1
                clothes[i] += 1
                answer += 1

    return answer