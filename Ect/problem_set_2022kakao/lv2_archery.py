import copy


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


def make_tree(tree, info, n, inf_idx=0, idx=1, score = 0):
    if n == 0:
        return 0
    elif inf_idx == len(info):
        return 0
    else:
        if inf_idx <= len(info) - 2:
            if info[inf_idx] + 1 <= n:
                if info[inf_idx] == 0:
                    shot_score = score + len(info) - 1 - inf_idx
                else:
                    shot_score = score + (len(info) - 1 - inf_idx) * 2
                tree[idx * 2] = (info[inf_idx] + 1, shot_score)
                tree[idx * 2 + 1] = (0, score)
                return make_tree(tree, info, n - info[inf_idx] - 1, inf_idx + 1, idx * 2, shot_score)\
                       + make_tree(tree, info, n, inf_idx + 1, idx * 2 + 1, score)
            else:
                tree[idx * 2 + 1] = (0, score)
                return make_tree(tree, info, n, inf_idx + 1, idx * 2, score)
        elif inf_idx == len(info) - 1:
            tree[idx * 2] = (n, score)
            tree[idx * 2 + 1] = (n, score)
            return 0


def solution3(n, info):
    # t22, 82.1점, 오답 8, 18, 21
    tree = [(0, 0) for _ in range(4097)]
    tree[1] = (0, 0)

    score = 0
    for v, s in zip(info, range(10, -1, -1)):
        score += s if v > 0 else 0
    make_tree(tree, info, n, score=-score)

    score_list = sorted(set(tree), key=lambda x: (-x[1], -x[0]))
    print("score_list:", score_list[:5])

    # 이길 수 없는 경우
    if score_list[0][1] == 0:
        return [-1]

    # 동일 점수 중 가장 뒤에 있는 index 검출 생략
    test = copy.deepcopy(tree)
    test.reverse()
    backward_idx = test.index(score_list[0])
    convert_idx = 4096 - backward_idx
    print("value check:", tree[convert_idx])
    del test

    answer = []
    while convert_idx > 1:
        answer.append(tree[convert_idx][0])
        convert_idx = convert_idx // 2
    answer.reverse()

    if len(answer) < 11:
        for _ in range(11 - len(answer)):
            answer.append(0)
    return answer


def solution4(n, info):
    # t25, max 10.94ms
    tree = [(0, 0) for _ in range(4097)]
    tree[1] = (0, 0)

    score = 0
    for v, s in zip(info, range(10, -1, -1)):
        score += s if v > 0 else 0
    make_tree(tree, info, n, score=-score)

    score_list = sorted(set(tree), key=lambda x: (-x[1], -x[0]))
    print("score_list:", score_list[:5])

    # 동점 비교
    max_score_list = []
    max_score = score_list[0][1]
    for s in score_list:
        if s[1] == max_score:
            max_score_list.append(s)
    print("max_list:", max_score_list)
    # 이길 수 없는 경우
    if max_score_list[0][1] == 0:
        return [-1]

    backward = copy.deepcopy(tree)
    backward.reverse()

    backward_idx = []
    for ms in max_score_list:
        start_idx = 0
        while True:
            try:
                backward_idx.append(backward.index(ms, start_idx))
                start_idx = backward_idx[-1] + 1
            except:
                break
    del backward

    convert_idx = [4096 - b for b in backward_idx]
    print("convert_idx:", convert_idx)
    print("value check:", tree[convert_idx[0]])

    answer = []
    for c_idx in convert_idx:
        tmp = ''
        first = tree[c_idx][0]
        while c_idx > 1:
            tmp += str(tree[c_idx][0])
            c_idx = c_idx // 2
        short = 11 - len(tmp)
        tmp = tmp.zfill(11)
        tmp = tmp[::-1]
        answer.append((short, first, tmp))

    print("answer_list:", sorted(answer, key=lambda x: (x[0], -x[1])))
    return list(map(int, list(sorted(answer, key=lambda x: (x[0], -x[1]))[0][2])))


print(solution4(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))