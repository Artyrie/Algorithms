from itertools import combinations
from collections import Counter


def solution(orders, course):
    # t5, 25점
    dic = {}
    candidate = []
    for idx1, order1 in zip(range(len(orders)), orders):
        set1 = set(list(order1))
        for idx2, order2 in zip(range(len(orders)), orders):
            if idx1 == idx2:
                continue
            inter = sorted(set1.intersection(set(order2)))
            if len(inter) > 2:
                for i in range(2, len(inter)):
                    if i in course:
                        comb = list(combinations(inter, i))
                        candidate.extend(comb)
            if len(inter) in course:
                try:
                    dic[tuple(inter)] += 1
                except:
                    dic[tuple(inter)] = 1

    key = dic.keys()
    for c in candidate:
        if c in key:
            dic[c] += 1
    answer = []
    check = [0, 0]  # freq, len
    items = sorted(dic.items(), key=lambda x: (-x[1], len(x[0])))
    tmp_max = 0
    tmp_len = 0
    for item in items:
        if tmp_max == 0:
            tmp_max = item[1]
            tmp_len = len(item[0])
        if tmp_len == len(item[0]) and tmp_max == item[1]:
            answer.append(''.join(item[0]))
        elif tmp_len != len(item[0]):
            tmp_max = item[1]
            tmp_len = len(item[0])
            answer.append(''.join(item[0]))
    return sorted(answer)


def solution2(orders, course):
    # t20, max 13.93ms
    dic = {}
    candidate = []
    for idx1, order1 in zip(range(len(orders)), orders):
        set1 = set(list(order1))
        for idx2, order2 in zip(range(len(orders)), orders):
            if idx1 == idx2:
                continue
            inter = sorted(set1.intersection(set(order2)))
            if len(inter) >= 2:
                for i in course:
                    if i > len(inter):
                        break
                    else:
                        comb = list(combinations(inter, i))
                        candidate.extend(comb)

    for c in candidate:
        key = ''.join(c)
        try:
            dic[key] += 1
        except:
            dic[key] = 1

    items = sorted(dic.items(),
                   key=lambda x: (len(x[0]), -x[1]))

    answer = []
    cur_max = 0
    cur_len = 0
    for item in items:
        if cur_max == 0:
            cur_max = item[1]
            cur_len = len(item[0])
        elif cur_len != len(item[0]):
            cur_max = item[1]
            cur_len = len(item[0])
        if item[1] == cur_max and len(item[0]) == cur_len:
            answer.append(item[0])
    return sorted(answer)


def solution3(orders, course):
    # t10, max 2.83ms
    candidate = [[] for _ in range(11)]
    for c_num in course:  # 개수 별 정렬
        for order in orders:
            comb = list(combinations(order, c_num))
            comb = [''.join(sorted(c)) for c in comb]
            candidate[c_num].extend(comb)

    answer = []
    for c_num in course:  # Count
        counts = Counter(candidate[c_num]).most_common()
        if counts:
            most_num = counts[0][1]
            if most_num < 2:
                break
            else:
                for el, cnt in counts:
                    if cnt == most_num:
                        answer.append(el)
                    else:
                        break
    return sorted(answer)