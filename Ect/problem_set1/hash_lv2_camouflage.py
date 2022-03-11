from itertools import combinations
from collections import Counter
from functools import reduce


def solution1(clothes):
    # 96.4점 t27, 시간 초과 t1
    tmp = [v[1] for v in clothes]
    count_clothes = list(Counter(tmp).values())
    answer = sum(count_clothes)
    for i in range(2, len(count_clothes) + 1):
        comb = list(combinations(count_clothes, i))
        for tup in comb:
            answer += reduce(lambda x, y: x * y, tup)
    return answer


def solution2(clothes):
    # 96.4점 t27, 시간 초과 t1, max 262.57ms
    tmp = [v[1] for v in clothes]
    count_clothes = list(Counter(tmp).values())
    answer = sum(count_clothes)
    for i in range(2, len(count_clothes) + 1):
        comb = list(combinations(count_clothes, i))
        for tup in comb:
            tmp = 1
            for t in tup:
                tmp *= t
            answer += tmp
    return answer


def solution3(clothes):
    # 96.4점 t27, 시간 초과 t1
    tmp = [v[1] for v in clothes]
    count_clothes = list(Counter(tmp).values())
    answer = sum(count_clothes)
    for i in range(2, len(count_clothes) + 1):
        comb = list(combinations(count_clothes, i))
        tmp = [reduce(lambda x, y: x * y, tup) for tup in comb]
        answer += sum(tmp)
    return answer


def solution4(clothes):
    # 96.4점 t27, 시간 초과 t1, max 390.03ms
    tmp = [v[1] for v in clothes]
    count_clothes = list(Counter(tmp).values())
    answer = sum(count_clothes)
    mul_dic = {}

    for i in range(2, len(count_clothes) + 1):
        comb = list(combinations(count_clothes, i))
        comb = [tuple(sorted(tup)) for tup in comb]
        comb = Counter(comb)

        for x, y in comb.items():
            if not x[:-1] in mul_dic.keys():
                tmp = 1

                for val in x:
                    tmp *= val
                mul_dic[x] = tmp
            else:
                mul_dic[x] = mul_dic[x[:-1]] * x[-1]
            answer += mul_dic[x] * y
    return answer


def solution5(clothes):
    # 96.4 t27, 시간 초과 1, max 4.36ms
    tmp = [v[1] for v in clothes]
    count_clothes = list(Counter(tmp).values())
    answer = 0
    non1 = []
    num1 = count_clothes.count(1)
    num1 = [1 for _ in range(num1)]
    for val in count_clothes:
        if val > 1:
            non1.append(val)
    for i in range(len(num1) + 1):
        if i == 0:
            comb_num1 = 1
        else:
            comb_num1 = len(list(combinations(num1, i)))

        for j in range(len(non1) + 1):
            if j == 0:
                comb_non1 = 1
                if i != 0:
                    answer += comb_num1 * comb_non1
            else:
                comb_non1 = list(combinations(non1, j))
                for tup in comb_non1:
                    tmp = 1
                    for t in tup:
                        tmp *= t
                    answer += tmp * comb_num1
    return answer


def solution6(clothes):
    # 100점, t28, max 0.05ms
    tmp = [v[1] for v in clothes]
    count_clothes = list(Counter(tmp).values())
    answer = 1
    for val in count_clothes:
        answer *= (val + 1)
    return answer - 1