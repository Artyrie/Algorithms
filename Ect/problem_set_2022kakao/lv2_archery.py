def solution1(n, info):
    # t15, 64.3점
    answer = [0 for i in range(11)]
    a_score = sum([s if v > 0 else 0 for v, s in zip(info, range(10, -1, -1))])
    l_score = 0
    score_done = 11

    while n > 0:
        print("=====")
        print(f"n : {n}, info : {info}")
        print(f"a score : {a_score}, l score : {l_score}")
        print(f"answer : {answer}")

        nps = []  # 발당 점수, 발수, 점수
        for val, s in zip(info, range(10, -1, -1)):
            if val > n:
                continue
            else:
                get_score = 2 * s if val > 0 else s
                nps.append((round(get_score / (val + 1), 2), val + 1, s))
        nps = sorted(nps, key=lambda x: (x[0], -x[2], -x[1]))
        print(nps)
        while True:
            if not nps:
                answer[10] += 1
                n -= 1
                break
            tmp = nps.pop()
            if tmp[1] <= n:
                l_score += tmp[2]
                a_score -= tmp[2] if tmp[1] > 1 else 0
                n -= tmp[1]
                answer[10 - tmp[2]] = tmp[1]
                info[10 - tmp[2]] = score_done
                break

    print(l_score, answer)
    if l_score > a_score:
        return answer
    else:
        return [-1]


def solution2(n, info):
    # t16, 60.7점
    answer = [0 for i in range(11)]
    a_score = sum([s if v > 0 else 0 for v, s in zip(info, range(10, -1, -1))])
    l_score = 0
    score_done = 11

    while n > 0:
        print("=====")
        print(f"n : {n}, info : {info}")
        print(f"a score : {a_score}, l score : {l_score}")
        print(f"answer : {answer}")

        nps = []  # 발당 점수, 발수, 점수, 점수 차
        for val, s in zip(info, range(10, -1, -1)):
            if val > n:
                continue
            else:
                get_score = 2 * s if val > 0 else s
                score_diff = a_score - l_score - s
                score_diff += -s if val > 0 else 0
                nps.append((round(get_score / (val + 1), 2), val + 1, s, score_diff))
        nps = sorted(nps, key=lambda x: (-x[3], x[0], -x[2], -x[1]))
        print(nps)
        while True:
            if not nps:
                answer[10] += 1
                n -= 1
                break
            tmp = nps.pop()
            if tmp[1] <= n:
                l_score += tmp[2]
                a_score -= tmp[2] if tmp[1] > 1 else 0
                n -= tmp[1]
                answer[10 - tmp[2]] = tmp[1]
                info[10 - tmp[2]] = score_done
                break

    if l_score > a_score:
        print(l_score, answer)
        return answer
    else:
        return [-1]

solution1(10, [8, 8, 1, 2, 3, 0, 2, 2, 2, 2, 2])